import unittest

from analyze import estimate_models, generate_data


class OLSLabTests(unittest.TestCase):
    def test_reproducible_data(self):
        first = generate_data(100, 42)
        second = generate_data(100, 42)
        self.assertTrue(first.equals(second))

    def test_models_fit_and_expected_columns(self):
        data = generate_data(200, 42)
        models = estimate_models(data)
        self.assertEqual(int(models["robust"].nobs), 200)
        self.assertIn("floor_area_sqft", models["robust"].params.index)
        self.assertTrue(models["robust"].bse.notna().all())

    def test_missing_columns_rejected(self):
        import pandas as pd

        with self.assertRaises(ValueError):
            estimate_models(pd.DataFrame({"annual_kwh": [1, 2]}))


if __name__ == "__main__":
    unittest.main()
