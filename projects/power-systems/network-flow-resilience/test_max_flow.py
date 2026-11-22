import unittest

from max_flow import maximum_flow, case_study


class MaximumFlowTests(unittest.TestCase):
    def test_case_study_flow_and_cut(self):
        value, source_side, flows, cut = case_study()
        self.assertAlmostEqual(value, 11.0)
        self.assertEqual(source_side, {"s", "a"})
        self.assertAlmostEqual(sum(edge[2] for edge in cut), value)
        flow_map = {(u, v): f for u, v, f in flows}
        self.assertEqual(flow_map, {
            ("s", "a"): 6.0,
            ("s", "b"): 5.0,
            ("a", "b"): 2.0,
            ("a", "t"): 4.0,
            ("b", "t"): 7.0,
        })

    def test_internal_arc_outage_preserves_connectivity_but_reduces_flow(self):
        nodes = ("s", "a", "b", "t")
        edges = (
            ("s", "a", 7), ("s", "b", 5),
            ("a", "t", 4), ("b", "t", 8),
        )
        value, source_side, _, cut = maximum_flow(nodes, edges, "s", "t")
        self.assertAlmostEqual(value, 9.0)
        self.assertNotIn("t", source_side)  # No residual s-t path remains.
        self.assertAlmostEqual(sum(edge[2] for edge in cut), value)

    def test_source_arc_outage(self):
        nodes = ("s", "a", "b", "t")
        edges = (
            ("s", "b", 5), ("a", "b", 2),
            ("a", "t", 4), ("b", "t", 8),
        )
        value, _, _, cut = maximum_flow(nodes, edges, "s", "t")
        self.assertAlmostEqual(value, 5.0)
        self.assertAlmostEqual(sum(edge[2] for edge in cut), value)

    def test_parallel_arcs(self):
        value, _, _, cut = maximum_flow(
            ("s", "t"), (("s", "t", 2), ("s", "t", 3)), "s", "t"
        )
        self.assertAlmostEqual(value, 5.0)
        self.assertAlmostEqual(sum(edge[2] for edge in cut), value)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            maximum_flow(("s", "t"), (("s", "t", -1),), "s", "t")
        with self.assertRaises(ValueError):
            maximum_flow(("s", "t"), (), "s", "s")
        with self.assertRaises(ValueError):
            maximum_flow(("s", "t"), (("s", "x", 1),), "s", "t")
        with self.assertRaises(ValueError):
            maximum_flow(("s", "t"), (("s", "t", float("nan")),), "s", "t")
        with self.assertRaises(ValueError):
            maximum_flow(("s", "t"), (("s", "t", float("inf")),), "s", "t")


if __name__ == "__main__":
    unittest.main()
