import csv
import tempfile
import unittest
from pathlib import Path

from plot_ppl_net_metering import create_figure


class PPLNetMeteringFigureTests(unittest.TestCase):
    def test_creates_png_and_svg_with_unknown_basis_point(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "series.csv"
            fields = ["year", "standard_net_metered_pv_capacity_mw", "pv_capacity_basis"]
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"year": 2015, "standard_net_metered_pv_capacity_mw": 76.686,
                                 "pv_capacity_basis": "not separately reported"})
                writer.writerow({"year": 2016, "standard_net_metered_pv_capacity_mw": 92.915,
                                 "pv_capacity_basis": "AC"})
                writer.writerow({"year": 2017, "standard_net_metered_pv_capacity_mw": 112.757,
                                 "pv_capacity_basis": "AC"})
            png, svg = create_figure(source, root / "figures")
            self.assertTrue(png.is_file())
            self.assertTrue(svg.is_file())
            self.assertGreater(png.stat().st_size, 1000)
            self.assertGreater(svg.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
