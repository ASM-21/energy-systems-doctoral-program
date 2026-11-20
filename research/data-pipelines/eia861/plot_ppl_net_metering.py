"""Create a source-aware figure of PPL's reported standard net-metered PV capacity."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_series(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Harmonized EIA series is empty.")
    return sorted(rows, key=lambda row: int(row["year"]))


def create_figure(input_csv: Path, output_dir: Path) -> tuple[Path, Path]:
    rows = load_series(input_csv)
    years = [int(row["year"]) for row in rows]
    capacity = [float(row["standard_net_metered_pv_capacity_mw"]) for row in rows]
    basis = [row["pv_capacity_basis"] for row in rows]
    ac_years = [year for year, item in zip(years, basis) if item == "AC"]
    ac_capacity = [value for value, item in zip(capacity, basis) if item == "AC"]
    unknown = [(year, value) for year, value, item in zip(years, capacity, basis)
               if item != "AC"]
    if not ac_years:
        raise ValueError("No AC-basis observations found.")

    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(11, 6.5), constrained_layout=True)
    ax.plot(ac_years, ac_capacity, marker="o", linewidth=2.2,
            label="Reported standard net-metered PV capacity (AC)")
    for year, value in unknown:
        ax.scatter([year], [value], marker="o", facecolors="none",
                   edgecolors="black", s=90, linewidths=1.8,
                   label="Capacity basis not separately reported")
        ax.annotate("AC/DC basis not reported", (year, value),
                    xytext=(12, 16), textcoords="offset points",
                    fontsize=9, arrowprops={"arrowstyle": "-", "lw": 0.8})
    ax.set_title("PPL Electric Utilities: Reported Standard Net-Metered PV Capacity")
    ax.set_xlabel("EIA Form 861 reporting year")
    ax.set_ylabel("Capacity (MW)")
    ax.set_xticks(years)
    ax.set_xlim(min(years) - 0.4, max(years) + 0.4)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False, loc="upper left")
    ax.text(
        0.01, -0.18,
        "Source: EIA Form 861 annual Net Metering schedule, utility ID 14715. "
        "2016–2025 observations report AC capacity; 2015 is shown separately "
        "because its AC/DC basis is not specified. This is not feeder hosting capacity.",
        transform=ax.transAxes, fontsize=8.5, va="top", wrap=True,
    )
    png_path = output_dir / "ppl-standard-net-metered-pv-capacity.png"
    svg_path = output_dir / "ppl-standard-net-metered-pv-capacity.svg"
    fig.savefig(png_path, dpi=220)
    fig.savefig(svg_path)
    plt.close(fig)
    return png_path, svg_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path,
                        default=Path("outputs/historical-net-metering/harmonized/ppl_net_metering_harmonized.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/historical-net-metering/figures"))
    args = parser.parse_args()
    png, svg = create_figure(args.input_csv, args.output_dir)
    print(f"PNG: {png.resolve()}")
    print(f"SVG: {svg.resolve()}")


if __name__ == "__main__":
    main()
