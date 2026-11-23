import unittest

from unit_commitment import DEFAULT_UNITS, solve_unit_commitment


class UnitCommitmentTests(unittest.TestCase):
    def test_integer_benchmark_schedule_and_costs(self):
        result = solve_unit_commitment()
        self.assertAlmostEqual(result["objective"], 6940.0)
        self.assertAlmostEqual(result["energy_cost"], 6100.0)
        self.assertAlmostEqual(result["no_load_cost"], 240.0)
        self.assertAlmostEqual(result["startup_cost"], 600.0)
        rows = {row["name"]: row["periods"] for row in result["schedules"]}
        self.assertEqual([round(p["dispatch_mw"]) for p in rows["G1"]], [80, 100])
        self.assertEqual([round(p["commitment"]) for p in rows["G1"]], [1, 1])
        self.assertEqual([round(p["startup"]) for p in rows["G1"]], [1, 0])
        self.assertEqual([round(p["dispatch_mw"]) for p in rows["G2"]], [0, 50])
        self.assertEqual([round(p["commitment"]) for p in rows["G2"]], [0, 1])
        self.assertEqual([round(p["startup"]) for p in rows["G2"]], [0, 1])

    def test_lp_relaxation_lower_bound_and_integrality_gap(self):
        result = solve_unit_commitment(relax_commitment=True)
        self.assertAlmostEqual(result["objective"], 6850.0)
        self.assertLess(result["objective"], solve_unit_commitment()["objective"])
        rows = {row["name"]: row["periods"] for row in result["schedules"]}
        self.assertAlmostEqual(rows["G1"][0]["commitment"], 0.8)
        self.assertAlmostEqual(rows["G2"][1]["commitment"], 0.5)

    def test_startup_cost_sensitivity(self):
        units = [dict(unit) for unit in DEFAULT_UNITS]
        units[0]["startup_cost"] = 1000.0
        result = solve_unit_commitment(units=units)
        self.assertAlmostEqual(result["objective"], 7440.0)
        self.assertAlmostEqual(result["schedules"][0]["periods"][0]["commitment"], 1.0)

    def test_lower_period_two_demand_avoids_second_unit(self):
        result = solve_unit_commitment(demand_mw=(80.0, 100.0))
        rows = {row["name"]: row["periods"] for row in result["schedules"]}
        self.assertAlmostEqual(result["objective"], 4300.0)
        self.assertEqual([round(p["commitment"]) for p in rows["G2"]], [0, 0])

    def test_initial_commitment_is_respected(self):
        result = solve_unit_commitment(demand_mw=(80.0,), initial_on=(1, 0))
        rows = {row["name"]: row["periods"] for row in result["schedules"]}
        self.assertEqual(round(rows["G1"][0]["startup"]), 0)

    def test_invalid_inputs(self):
        for kwargs in [
            {"demand_mw": ()},
            {"demand_mw": (-1, 80)},
            {"initial_on": (0,)},
            {"units": [dict(DEFAULT_UNITS[0], minimum_mw=120)]},
            {"units": [dict(DEFAULT_UNITS[0], maximum_mw=float("nan"))]},
        ]:
            with self.assertRaises(ValueError):
                solve_unit_commitment(**kwargs)

    def test_infeasible_demand(self):
        with self.assertRaises(ValueError):
            solve_unit_commitment(demand_mw=(80.0, 250.0))


if __name__ == "__main__":
    unittest.main()
