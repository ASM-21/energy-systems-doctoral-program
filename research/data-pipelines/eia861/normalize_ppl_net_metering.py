"""Create a conservative harmonized PPL net-metering series from raw EIA rows."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path


def parse_number(value: str | None) -> float | None:
    if value is None or str(value).strip() in ("", ".", "..", "NA", "N/A"):
        return None
    return float(str(value).replace(",", "").strip())


def field_ending(row: dict, suffixes: tuple[str, ...]) -> tuple[str | None, str | None]:
    matches = [(key, row[key]) for key in row
               if any(key == suffix or key.endswith("__" + suffix) for suffix in suffixes)]
    if not matches:
        return None, None
    if len(matches) > 1:
        populated = [(key, value) for key, value in matches if value not in ("", ".", None)]
        if len(populated) == 1:
            return populated[0]
        if len(populated) > 1:
            raise ValueError(f"Ambiguous populated fields for suffixes {suffixes}: {[key for key, _ in populated]}")
        return matches[0]
    return matches[0]


def normalized_row(row: dict) -> dict:
    year = int(row["year"])
    capacity_field, capacity_raw = field_ending(row, ("Photovoltaic__Capacity_MW__Total",))
    if capacity_field is None:
        raise ValueError(f"No standard PV capacity total field found for {year}")
    capacity = parse_number(capacity_raw)
    if capacity is None:
        raise ValueError(f"Standard PV capacity is missing for {year}")

    count_field, count_raw = field_ending(row, (
        "Photovoltaic__Customers__Total", "Photovoltaic__Installations__Total"
    ))
    count_value = parse_number(count_raw)
    count_measure = "customers" if count_field and "Customers" in count_field else (
        "installations" if count_field else "not reported"
    )

    virtual_field, virtual_raw = field_ending(row, ("Photovoltaic__Virtual_Capacity_(MW)__Total",))
    if virtual_field is not None:
        virtual_capacity = parse_number(virtual_raw)
        virtual_measure = "combined virtual PV capacity; size bands not separated"
    else:
        large_field, large_raw = field_ending(row, (
            "Photovoltaic__Virtual_Capacity-_1_MW_and_over_(MW)__Total",
        ))
        small_field, small_raw = field_ending(row, (
            "Photovoltaic__Virtual_Capacity-_under_1_MW_(MW)__Total",
        ))
        large = parse_number(large_raw)
        small = parse_number(small_raw)
        if large is None and small is None:
            virtual_capacity = None
        else:
            virtual_capacity = round((large or 0.0) + (small or 0.0), 6)
        virtual_field = ";".join(field for field in (large_field, small_field) if field)
        virtual_measure = "sum of virtual PV capacity >=1 MW and <1 MW categories"

    type_field, type_raw = field_ending(row, ("Photovoltaic__Capacity_MW__Type",))
    capacity_basis = type_raw if type_raw not in (None, "", ".") else "not separately reported"
    state_field, state_raw = field_ending(row, ("Utility_Characteristics__State", "State"))
    ba_field, ba_raw = field_ending(row, ("Utility_Characteristics__BA_Code", "BA_Code"))
    alltech_field, alltech_raw = field_ending(row, (
        "All_Technologies__Capacity_MW__Total", "Total__Capacity_MW"
    ))

    return {
        "year": year,
        "eia_utility_id": row["eia_utility_id"],
        "utility_name": row["utility_name"],
        "state": state_raw or "",
        "balancing_authority": ba_raw or "",
        "standard_net_metered_pv_capacity_mw": capacity,
        "pv_count_value": count_value,
        "pv_count_measure": count_measure,
        "virtual_pv_capacity_mw": virtual_capacity,
        "virtual_pv_measure": virtual_measure,
        "all_technology_net_metered_capacity_mw": parse_number(alltech_raw),
        "pv_capacity_basis": capacity_basis,
        "source_workbook": row["source_workbook"],
        "source_sheet": row["source_sheet"],
        "source_row": row["source_row"],
        "archive_sha256": row["archive_sha256"],
        "standard_pv_capacity_source_field": capacity_field,
        "pv_count_source_field": count_field or "",
        "virtual_pv_source_field": virtual_field or "",
        "all_technology_capacity_source_field": alltech_field or "",
        "capacity_basis_source_field": type_field or "",
        "state_source_field": state_field or "",
        "balancing_authority_source_field": ba_field or "",
    }


def normalize_file(input_csv: Path, output_dir: Path) -> dict:
    with input_csv.open(newline="", encoding="utf-8") as handle:
        raw_rows = list(csv.DictReader(handle))
    if not raw_rows:
        raise ValueError("Raw historical PPL net-metering extract is empty")
    rows = sorted((normalized_row(row) for row in raw_rows), key=lambda row: row["year"])
    years = [row["year"] for row in rows]
    if len(years) != len(set(years)):
        raise ValueError("Expected exactly one PPL utility-level net-metering row per year")
    for previous, current in zip(rows, rows[1:]):
        comparable_basis = (
            previous["pv_capacity_basis"] == current["pv_capacity_basis"]
            and current["pv_capacity_basis"] != "not separately reported"
        )
        if comparable_basis:
            current["annual_standard_pv_capacity_change_mw"] = round(
                current["standard_net_metered_pv_capacity_mw"] - previous["standard_net_metered_pv_capacity_mw"], 6
            )
            current["annual_standard_pv_capacity_change_pct"] = round(
                100 * current["annual_standard_pv_capacity_change_mw"] /
                previous["standard_net_metered_pv_capacity_mw"], 6
            )
        else:
            current["annual_standard_pv_capacity_change_mw"] = None
            current["annual_standard_pv_capacity_change_pct"] = None
    rows[0]["annual_standard_pv_capacity_change_mw"] = None
    rows[0]["annual_standard_pv_capacity_change_pct"] = None
    output_dir.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with (output_dir / "ppl_net_metering_harmonized.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    start, end = rows[0], rows[-1]
    ac_rows = [row for row in rows if row["pv_capacity_basis"] == "AC"]
    ac_start = ac_rows[0] if ac_rows else None
    ac_years_span = end["year"] - ac_start["year"] if ac_start else 0
    ac_cagr = ((end["standard_net_metered_pv_capacity_mw"] / ac_start["standard_net_metered_pv_capacity_mw"]) ** (1 / ac_years_span) - 1) if ac_start and ac_years_span else None
    nominal_years_span = end["year"] - start["year"]
    nominal_cagr = ((end["standard_net_metered_pv_capacity_mw"] / start["standard_net_metered_pv_capacity_mw"]) ** (1 / nominal_years_span) - 1) if nominal_years_span else None
    summary = {
        "utility_id": start["eia_utility_id"],
        "utility_name": start["utility_name"],
        "observations": len(rows),
        "start_year": start["year"],
        "end_year": end["year"],
        "standard_net_metered_pv_capacity_start_mw": start["standard_net_metered_pv_capacity_mw"],
        "standard_net_metered_pv_capacity_end_mw": end["standard_net_metered_pv_capacity_mw"],
        "reported_nominal_capacity_change_mw_2015_2025": round(end["standard_net_metered_pv_capacity_mw"] - start["standard_net_metered_pv_capacity_mw"], 6),
        "reported_nominal_capacity_change_pct_2015_2025": round(100 * (end["standard_net_metered_pv_capacity_mw"] / start["standard_net_metered_pv_capacity_mw"] - 1), 6),
        "reported_nominal_capacity_cagr_pct_2015_2025": round(100 * nominal_cagr, 6) if nominal_cagr is not None else None,
        "ac_capacity_start_year": ac_start["year"] if ac_start else None,
        "ac_capacity_start_mw": ac_start["standard_net_metered_pv_capacity_mw"] if ac_start else None,
        "ac_capacity_end_year": end["year"] if ac_start else None,
        "ac_capacity_end_mw": end["standard_net_metered_pv_capacity_mw"] if ac_start else None,
        "ac_capacity_change_mw": round(end["standard_net_metered_pv_capacity_mw"] - ac_start["standard_net_metered_pv_capacity_mw"], 6) if ac_start else None,
        "ac_capacity_change_pct": round(100 * (end["standard_net_metered_pv_capacity_mw"] / ac_start["standard_net_metered_pv_capacity_mw"] - 1), 6) if ac_start else None,
        "ac_capacity_cagr_pct": round(100 * ac_cagr, 6) if ac_cagr is not None else None,
        "count_measure_break": "EIA field changes from Customers through 2020 to Installations beginning 2021; do not treat the count series as perfectly homogeneous without reviewing survey instructions.",
        "capacity_basis_break": "2015 does not separately report the PV capacity AC/DC type in this row; 2016 onward reports AC. Treat 2015 basis as unknown.",
        "virtual_capacity_break": "2016-2022 reports a combined virtual PV capacity field; 2023 onward separates >=1 MW and <1 MW categories. 2015 does not report a virtual PV field in the extracted row.",
        "causal_warning": "This is descriptive reported capacity, not a causal estimate of any PPL program, tariff, interconnection reform, or hosting-capacity change.",
        "engineering_warning": "Utility-level net-metered PV capacity is not feeder hosting capacity, installed inverter capacity, export energy, or interconnection queue outcomes."
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"PPL standard net-metered PV capacity: {summary['standard_net_metered_pv_capacity_start_mw']:.3f} MW ({summary['start_year']}) -> {summary['standard_net_metered_pv_capacity_end_mw']:.3f} MW ({summary['end_year']})")
    print(f"AC-basis change: {summary['ac_capacity_change_mw']:.3f} MW; CAGR {summary['ac_capacity_cagr_pct']:.2f}%")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, default=Path("outputs/historical-net-metering/ppl_net_metering_raw.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/historical-net-metering/harmonized"))
    args = parser.parse_args()
    summary = normalize_file(args.input_csv, args.output_dir)
    print(f"Normalized observations: {summary['observations']}")


if __name__ == "__main__":
    main()
