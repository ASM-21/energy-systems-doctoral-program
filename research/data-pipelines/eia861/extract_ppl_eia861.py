"""Extract PPL Electric utility-ID rows from the EIA-861 workbook package."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from openpyxl import load_workbook

TARGET_UTILITY_ID = "14715"
IGNORED_HEADER_LABELS = {"utility characteristics"}

def normalize_label(value) -> str:
    text = str(value).strip()
    return "_".join(text.replace("\n", " ").replace("/", " ").split())

def find_header_row(sheet) -> int | None:
    for row_index in range(1, min(sheet.max_row or 1, 8) + 1):
        values = [str(cell.value).strip().lower() for cell in sheet[row_index] if cell.value is not None]
        if any("utility number" == value for value in values) and any("utility name" == value for value in values):
            return row_index
    return None

def build_headers(sheet, header_row: int) -> list[str]:
    """Build semantically grouped headers, propagating merged Excel headings."""
    grid = [
        [sheet.cell(row_index, column).value
         for column in range(1, (sheet.max_column or 1) + 1)]
        for row_index in range(1, header_row + 1)
    ]
    # Merged group labels (e.g. Photovoltaic / Capacity MW / Residential)
    # are stored only in the top-left cell in Excel. Propagate them across
    # their merged ranges so each output field remains semantically distinct.
    merged_ranges = getattr(sheet, "merged_cells", None)
    if merged_ranges is not None:
        for merged in merged_ranges.ranges:
            if merged.min_row > header_row:
                continue
            anchor = sheet.cell(merged.min_row, merged.min_col).value
            if anchor is None:
                continue
            for row_index in range(merged.min_row, min(merged.max_row, header_row) + 1):
                for column in range(merged.min_col, merged.max_col + 1):
                    grid[row_index - 1][column - 1] = anchor

    headers = []
    for column in range(1, (sheet.max_column or 1) + 1):
        parts = []
        for row_index in range(1, header_row + 1):
            value = grid[row_index - 1][column - 1]
            if value is None:
                continue
            label = normalize_label(value)
            if not label or label.lower() in IGNORED_HEADER_LABELS or label.lower() == "utility characteristics":
                continue
            if label not in parts:
                parts.append(label)
        headers.append("__".join(parts) if parts else f"column_{column}")
    return headers
def extract_ppl_rows(workbooks_dir: Path, output_dir: Path, utility_id: str = TARGET_UTILITY_ID) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    long_rows = []
    coverage = []
    for workbook_path in sorted(workbooks_dir.glob("*.xlsx")):
        workbook = load_workbook(workbook_path, read_only=False, data_only=True)
        for sheet in workbook.worksheets:
            header_row = find_header_row(sheet)
            if header_row is None:
                coverage.append({"workbook": workbook_path.name, "sheet": sheet.title,
                                 "header_row": "", "utility_id_column_found": False,
                                 "ppl_rows_found": 0, "status": "no utility-number/name header"})
                continue
            headers = build_headers(sheet, header_row)
            utility_columns = [i for i, header in enumerate(headers)
                               if header.lower().endswith("utility_number") or header.lower() == "utility_number"]
            if not utility_columns:
                coverage.append({"workbook": workbook_path.name, "sheet": sheet.title,
                                 "header_row": header_row, "utility_id_column_found": False,
                                 "ppl_rows_found": 0, "status": "utility-number column not identified"})
                continue
            utility_col = utility_columns[0]
            name_columns = [i for i, header in enumerate(headers) if header.lower().endswith("utility_name")]
            name_col = name_columns[0] if name_columns else None
            hits = 0
            for row_number, values in enumerate(sheet.iter_rows(min_row=header_row + 1, values_only=True),
                                                 start=header_row + 1):
                if utility_col >= len(values) or values[utility_col] is None:
                    continue
                if str(values[utility_col]).strip() != str(utility_id):
                    continue
                hits += 1
                utility_name = str(values[name_col]).strip() if name_col is not None and name_col < len(values) else ""
                if utility_name and "PPL Electric" not in utility_name and utility_id == TARGET_UTILITY_ID:
                    raise ValueError(f"EIA utility ID {utility_id} mapped to unexpected name {utility_name!r} in {workbook_path.name}/{sheet.title}.")
                for index, value in enumerate(values):
                    if index >= len(headers):
                        continue
                    long_rows.append({
                        "eia_utility_id": utility_id,
                        "utility_name": utility_name,
                        "workbook": workbook_path.name,
                        "sheet": sheet.title,
                        "source_row": row_number,
                        "field": headers[index],
                        "value": "" if value is None else str(value),
                    })
            coverage.append({"workbook": workbook_path.name, "sheet": sheet.title,
                             "header_row": header_row, "utility_id_column_found": True,
                             "ppl_rows_found": hits,
                             "status": "PPL rows found" if hits else "no PPL row; absence is not zero"})
        workbook.close()
    with (output_dir / "ppl_eia861_2025_long.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["eia_utility_id", "utility_name", "workbook", "sheet", "source_row", "field", "value"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(long_rows)
    with (output_dir / "ppl_eia861_2025_coverage.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["workbook", "sheet", "header_row", "utility_id_column_found", "ppl_rows_found", "status"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(coverage)
    result = {"target_utility_id": utility_id, "sheets_scanned": len(coverage),
              "sheets_with_ppl_rows": sum(int(row["ppl_rows_found"]) > 0 for row in coverage),
              "long_form_records": len(long_rows)}
    (output_dir / "extract_summary.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbooks-dir", type=Path, default=Path("data/eia861-2025/workbooks"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/ppl-eia861-2025"))
    parser.add_argument("--utility-id", default=TARGET_UTILITY_ID)
    args = parser.parse_args()
    result = extract_ppl_rows(args.workbooks_dir, args.output_dir, args.utility_id)
    print(f"EIA utility {args.utility_id}: {result['sheets_with_ppl_rows']} worksheets with rows; {result['long_form_records']} long-form records")
    print(f"Extract: {args.output_dir.resolve()}")

if __name__ == "__main__":
    main()