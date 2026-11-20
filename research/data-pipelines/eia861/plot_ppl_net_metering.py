"""Create a source-aware figure of PPL's reported standard net-metered PV capacity."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "none"
matplotlib.rcParams["svg.hashsalt"] = "ppl-eia861-series"
import matplotlib.pyplot as plt


def load_series(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Harmonized EIA series is empty.")
    return sorted(rows, key=lambda row: int(row["year"]))


def write_source_aware_svg(rows: list[dict], path: Path) -> None:
    width, height = 1000, 600
    left, right, top, bottom = 100, 40, 72, 112
    plot_width, plot_height = width - left - right, height - top - bottom
    years = [int(row["year"]) for row in rows]
    values = [float(row["standard_net_metered_pv_capacity_mw"]) for row in rows]
    bases = [row["pv_capacity_basis"] for row in rows]
    x = lambda year: left + (year - min(years)) * plot_width / (max(years) - min(years))
    y = lambda value: top + plot_height - value * plot_height / 600.0
    ac_points = [(year, value) for year, value, basis in zip(years, values, bases) if basis == "AC"]
    unknown_points = [(year, value) for year, value, basis in zip(years, values, bases) if basis != "AC"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="500" y="34" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold">PPL Electric Utilities: Reported Standard Net-Metered PV Capacity</text>',
    ]
    for tick in range(0, 601, 100):
        yy = y(tick)
        parts.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{width-right}" y2="{yy:.1f}" stroke="#d8d8d8" stroke-width="1"/>')
        parts.append(f'<text x="{left-14}" y="{yy+5:.1f}" text-anchor="end" font-family="Arial,sans-serif" font-size="13">{tick}</text>')
    for year in years:
        xx = x(year)
        parts.append(f'<line x1="{xx:.1f}" y1="{top}" x2="{xx:.1f}" y2="{height-bottom}" stroke="#eeeeee" stroke-width="1"/>')
        parts.append(f'<text x="{xx:.1f}" y="{height-bottom+24}" text-anchor="middle" font-family="Arial,sans-serif" font-size="12">{year}</text>')
    parts.extend([
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#333" stroke-width="1.5"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#333" stroke-width="1.5"/>',
        f'<text x="{(left+width-right)/2}" y="{height-bottom+55}" text-anchor="middle" font-family="Arial,sans-serif" font-size="14">EIA Form 861 reporting year</text>',
        f'<text x="28" y="{top+plot_height/2}" text-anchor="middle" transform="rotate(-90 28 {top+plot_height/2})" font-family="Arial,sans-serif" font-size="14">Capacity (MW)</text>',
    ])
    ac_coords = " ".join(f'{x(year):.1f},{y(value):.1f}' for year, value in ac_points)
    parts.append(f'<polyline points="{ac_coords}" fill="none" stroke="#1f77b4" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    for year, value in ac_points:
        parts.append(f'<circle cx="{x(year):.1f}" cy="{y(value):.1f}" r="5" fill="#1f77b4"/>')
    for year, value in unknown_points:
        parts.append(f'<circle cx="{x(year):.1f}" cy="{y(value):.1f}" r="6" fill="white" stroke="#222" stroke-width="2"/>')
        parts.append(f'<text x="{x(year)+16:.1f}" y="{y(value)-18:.1f}" font-family="Arial,sans-serif" font-size="12">AC/DC basis not reported</text>')
    parts.extend([
        '<line x1="125" y1="80" x2="165" y2="80" stroke="#1f77b4" stroke-width="3"/>',
        '<circle cx="145" cy="80" r="4" fill="#1f77b4"/>',
        '<text x="175" y="85" font-family="Arial,sans-serif" font-size="12">Reported standard net-metered PV capacity (AC)</text>',
        '<circle cx="145" cy="103" r="5" fill="white" stroke="#222" stroke-width="2"/>',
        '<text x="175" y="108" font-family="Arial,sans-serif" font-size="12">Capacity basis not separately reported</text>',
        '<text x="100" y="550" font-family="Arial,sans-serif" font-size="11" fill="#444">Source: EIA Form 861 annual Net Metering schedule, utility ID 14715. 2016–2025 observations report AC capacity.</text>',
        '<text x="100" y="568" font-family="Arial,sans-serif" font-size="11" fill="#444">2015 is shown separately because its AC/DC basis is not specified. This is not feeder hosting capacity.</text>',
        '</svg>',
    ])
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


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
    plt.close(fig)
    write_source_aware_svg(rows, svg_path)
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
