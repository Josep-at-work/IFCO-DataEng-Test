import pytest
import pandas as pd
import json
from main import extract_full_name, add_full_name_column  

@pytest.mark.parametrize(
    "json_string, expected",
    [
        ('[{"contact_name": "Curtis", "contact_surname": "Galagan"}]', "Curtis Galagan"),
        ('[{"contact_name": "", "contact_surname": "Doe"}]', "John Doe"),  # Missing first name
        ('[{"contact_name": "John", "contact_surname": ""}]', "John Doe"),  # Missing last name
        ('[{"contact_name": "", "contact_surname": ""}]', "John Doe"),  # Missing both names
        ('[]', "John Doe"),  # Empty list
        ('invalid_json', "John Doe"),  # Invalid JSON format
        ('null', "John Doe"),  # Null value
    ],
)
def test_extract_full_name(json_string, expected):
    """Test that extract_full_name correctly extracts full names or returns 'John Doe' when needed."""
    assert extract_full_name(json_string) == expected


def test_add_full_name_column():
    """Test add_full_name_column ensures correct dataframe transformation."""
    
    # Sample input DataFrame
    data = {
        "order_id": [1, 2, 3],
        "contact_data": [
            '[{"contact_name": "Alice", "contact_surname": "Smith"}]',
            '[{"contact_name": "", "contact_surname": "Doe"}]',  # Missing first name
            'invalid_json',  # Invalid JSON
        ],
    }
    df = pd.DataFrame(data)
    
    # Expected output DataFrame
    expected_data = {
        "order_id": [1, 2, 3],
        "contact_full_name": ["Alice Smith", "John Doe", "John Doe"],
    }
    expected_df = pd.DataFrame(expected_data)
    
    # Apply function
    result_df = add_full_name_column(df)

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)
