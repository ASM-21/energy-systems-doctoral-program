import unittest

from frequency_response import (
    euler_stability_limit,
    eigenvalues_2x2,
    simulate_euler,
    simulate_rk4,
    state_matrix,
    steady_state,
)


class FrequencyResponseTests(unittest.TestCase):
    def test_state_matrix_and_eigenvalues(self):
        matrix = state_matrix()
        self.assertAlmostEqual(matrix[0][0], -0.2)
        values = eigenvalues_2x2(matrix)
        for value in values:
            self.assertAlmostEqual(value.real, -1.1, places=10)
            self.assertAlmostEqual(abs(value.imag), 2.681417535, places=6)

    def test_steady_state(self):
        frequency, mechanical = steady_state(0.01)
        self.assertAlmostEqual(frequency, -0.01 / 21.0)
        self.assertAlmostEqual(mechanical, 0.01 * 20.0 / 21.0)

    def test_rk4_converges_to_steady_state(self):
        expected = steady_state(0.01)
        actual = simulate_rk4(load_step=0.01, duration=10.0, step=0.001)
        self.assertAlmostEqual(actual[0], expected[0], delta=2e-6)
        self.assertAlmostEqual(actual[1], expected[1], delta=2e-6)

    def test_euler_stability_boundary(self):
        limit = euler_stability_limit(state_matrix())
        self.assertAlmostEqual(limit, 2.2 / 8.4, places=10)
        self.assertLess(abs(simulate_euler((1.0, 0.0), 5.0, 0.1)[0]), 1.0)
        unstable = simulate_euler((1.0, 0.0), 5.0, 0.3)
        self.assertGreater(abs(unstable[0]) + abs(unstable[1]), 1.0)

    def test_custom_inertia_is_used_consistently(self):
        expected = steady_state(0.01)
        actual = simulate_rk4(
            load_step=0.01, duration=10.0, step=0.001, inertia=10.0
        )
        self.assertAlmostEqual(actual[0], expected[0], delta=2e-6)
        self.assertAlmostEqual(actual[1], expected[1], delta=2e-6)
        self.assertNotEqual(state_matrix(inertia=10.0), state_matrix())

    def test_euler_integrates_fractional_final_step(self):
        matrix = ((-1.0, 0.0), (0.0, -2.0))
        actual = simulate_euler((1.0, 1.0), duration=0.25, step=0.1, matrix=matrix)
        self.assertAlmostEqual(actual[0], 0.9 * 0.9 * 0.95)
        self.assertAlmostEqual(actual[1], 0.8 * 0.8 * 0.9)

    def test_nonfinite_inputs_rejected(self):
        with self.assertRaises(ValueError):
            state_matrix(inertia=float("inf"))
        with self.assertRaises(ValueError):
            simulate_rk4(duration=float("nan"))
        with self.assertRaises(ValueError):
            simulate_euler((1.0, 0.0), duration=1.0, step=float("inf"))

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            state_matrix(inertia=0)
        with self.assertRaises(ValueError):
            steady_state(0.01, droop=0)
        with self.assertRaises(ValueError):
            simulate_rk4(step=0)


if __name__ == "__main__":
    unittest.main()
