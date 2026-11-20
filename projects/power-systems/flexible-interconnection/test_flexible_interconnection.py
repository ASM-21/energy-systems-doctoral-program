import unittest
from pathlib import Path
from flexible_interconnection import load_profile, export_envelopes, solve_scenario

DATA = Path(__file__).parent / "data" / "day_ahead_profile.csv"


class FlexibleInterconnectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = load_profile(DATA)
        cls.envelopes = export_envelopes(cls.profile)

    def test_envelopes_respect_physical_headroom(self):
        headroom = [1.0 - row["existing_feeder_net_export_mw"] for row in self.profile]
        for name, values in self.envelopes.items():
            if name != "firm_upgrade_1.50_mw":
                for actual, physical in zip(values, headroom):
                    self.assertLessEqual(actual, physical + 1e-9)

    def test_dynamic_envelope_tracks_baseline_feeder_conditions(self):
        dynamic = self.envelopes["dynamic_operating_envelope"]
        self.assertGreater(dynamic[0], dynamic[13])
        self.assertAlmostEqual(dynamic[13], 1.0 - self.profile[13]["existing_feeder_net_export_mw"])

    def test_upgrade_utilizes_at_least_as_much_pv_as_fixed_limit(self):
        fixed = solve_scenario(self.profile, self.envelopes["fixed_0.35_mw"])
        upgrade = solve_scenario(self.profile, self.envelopes["firm_upgrade_1.50_mw"])
        self.assertGreaterEqual(
            upgrade["summary"]["pv_utilized_mwh"],
            fixed["summary"]["pv_utilized_mwh"] - 1e-7,
        )

    def test_dispatch_respects_export_limit_and_soc_cycle(self):
        for name, limit in self.envelopes.items():
            result = solve_scenario(self.profile, limit)
            for row in result["hourly"]:
                self.assertLessEqual(row["grid_export_mw"], row["export_limit_mw"] + 1e-7)
                self.assertGreaterEqual(row["soc_end_mwh"], -1e-7)
                self.assertLessEqual(row["soc_end_mwh"], 1.5 + 1e-7)
                self.assertFalse(row["battery_charge_mw"] > 1e-6 and row["battery_discharge_mw"] > 1e-6)
            self.assertAlmostEqual(result["summary"]["initial_soc_mwh"], result["summary"]["terminal_soc_mwh"], places=7)

    def test_rejects_baseline_that_already_exceeds_feeder_limit(self):
        bad = [dict(row) for row in self.profile]
        bad[12]["existing_feeder_net_export_mw"] = 1.1
        with self.assertRaises(ValueError):
            export_envelopes(bad)

    def test_synthetic_case_exposes_curtailment_and_upgrade_tradeoff(self):
        fixed = solve_scenario(self.profile, self.envelopes["fixed_0.35_mw"])
        dynamic = solve_scenario(self.profile, self.envelopes["dynamic_operating_envelope"])
        upgrade = solve_scenario(self.profile, self.envelopes["firm_upgrade_1.50_mw"])
        self.assertGreater(fixed["summary"]["pv_curtailment_mwh"], 0.0)
        self.assertLessEqual(
            upgrade["summary"]["pv_curtailment_mwh"],
            fixed["summary"]["pv_curtailment_mwh"] + 1e-7,
        )
        self.assertGreaterEqual(dynamic["summary"]["pv_curtailment_mwh"], 0.0)

    def test_battery_reduces_curtailment_under_fixed_export_limit(self):
        limit = self.envelopes["fixed_0.35_mw"]
        with_battery = solve_scenario(self.profile, limit)
        without_battery = solve_scenario(
            self.profile, limit, battery_power_mw=0.0, battery_energy_mwh=0.0
        )
        self.assertLess(
            with_battery["summary"]["pv_curtailment_mwh"],
            without_battery["summary"]["pv_curtailment_mwh"],
        )


if __name__ == "__main__":
    unittest.main()
