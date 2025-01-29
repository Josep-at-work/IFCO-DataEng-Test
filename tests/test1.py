import pandas as pd
import unittest
from main import calculate_crate_distribution

# Test
class TestCrateDistribution(unittest.TestCase):
    
    def setUp(self):
        """
        Sample data.
        """
        self.test_data = pd.DataFrame({
            "company_id": ["C1", "C1", "C2", "C1", "C2", "C3", "C3", "C3"],
            "crate_type": ["plastic", "wood", "plastic", "plastic", "wood", "plastic", "plastic", "wood"],
        })
        
        self.expected_output = pd.DataFrame({
            "company_id": ["C1", "C1", "C2", "C2", "C3", "C3"],
            "crate_type": ["plastic", "wood", "plastic", "wood", "plastic", "wood"],
            "count_orders": [2, 1, 1, 1, 2, 1]
        }).sort_values(by=["company_id", "crate_type"]).reset_index(drop=True)

    def test_calculate_crate_distribution(self):
        """
        Validate the function
        """
        # Llamar a la función
        result = calculate_crate_distribution(self.test_data)
        
        # Sort results to properly compare the dataframes.
        result = result.sort_values(by=["company_id", "crate_type"]).reset_index(drop=True)
        
        # Validate column names
        self.assertListEqual(list(result.columns), ["company_id", "crate_type", "count_orders"])
        
        # Validate dataframe length
        self.assertEqual(len(result), len(self.expected_output))
        
        # Validte values
        pd.testing.assert_frame_equal(result, self.expected_output)

if __name__ == "__main__":
    unittest.main()
