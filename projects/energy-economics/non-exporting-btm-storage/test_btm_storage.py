import unittest
from pathlib import Path
from btm_storage import load_profile, solve_btm_storage


class BTMStorageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = load_profile(Path(__file__).parent / "data" / "daily_profile.csv")

    def test_no_export_and_energy_balance(self):
        result = solve_btm_storage(self.profile["load_kw"], self.profile["pv_kw"],
                                   self.profile["price_usd_per_mwh"],
                                   power_kw=80, energy_kwh=160, initial_soc_kwh=80)
        self.assertGreaterEqual(min(result["grid_import_kw"]), -1e-7)
        self.assertAlmostEqual(result["initial_soc_kwh"], 80, places=6)
        self.assertAlmostEqual(result["final_soc_kwh"], 80, places=6)
        self.assertGreaterEqual(result["minimum_soc_kwh"], -1e-7)
        self.assertLessEqual(result["maximum_soc_kwh"], 160 + 1e-7)
        for load, pv, grid, charge, discharge, curtail in zip(
            self.profile["load_kw"], self.profile["pv_kw"], result["grid_import_kw"],
            result["battery_charge_kw"], result["battery_discharge_kw"],
            result["pv_curtailment_kw"]):
            self.assertAlmostEqual(grid + discharge + pv - curtail, load + charge, places=6)

    def test_battery_reduces_pv_curtailment(self):
        baseline = solve_btm_storage(self.profile["load_kw"], self.profile["pv_kw"],
                                     self.profile["price_usd_per_mwh"],
                                     power_kw=0, energy_kwh=0, initial_soc_kwh=0)
        battery = solve_btm_storage(self.profile["load_kw"], self.profile["pv_kw"],
                                    self.profile["price_usd_per_mwh"],
                                    power_kw=80, energy_kwh=160, initial_soc_kwh=80)
        self.assertLess(battery["pv_curtailed_mwh"], baseline["pv_curtailed_mwh"])
        self.assertGreater(battery["battery_charge_mwh"], 0)
        self.assertGreater(battery["battery_discharge_mwh"], 0)

    def test_zero_battery_matches_no_storage_balance(self):
        result = solve_btm_storage(self.profile["load_kw"], self.profile["pv_kw"],
                                   self.profile["price_usd_per_mwh"],
                                   power_kw=0, energy_kwh=0, initial_soc_kwh=0)
        self.assertAlmostEqual(result["battery_charge_mwh"], 0)
        self.assertAlmostEqual(result["battery_discharge_mwh"], 0)
        self.assertGreaterEqual(min(result["grid_import_kw"]), -1e-7)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            solve_btm_storage([1, 2], [1], [10, 20], power_kw=1, energy_kwh=1)
        with self.assertRaises(ValueError):
            solve_btm_storage([1], [1], [10], power_kw=1, energy_kwh=1, eta_charge=0)
        with self.assertRaises(ValueError):
            solve_btm_storage([1], [1], [10], power_kw=1, energy_kwh=1, initial_soc_kwh=2)


if __name__ == "__main__":
    unittest.main()