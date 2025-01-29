import pytest
import pandas as pd
import json
from main import extract_address, add_address_column 

# Test cases for extract_address function
@pytest.mark.parametrize("json_input, expected_output", [
    ('[{"city": "Barcelona", "cp": "08001"}]', "Barcelona, 08001"),
    ('[{"city": "Madrid", "cp": ""}]', "Madrid, UNK00"),
    ('[{"city": "", "cp": "28001"}]', "Unknown, 28001"),
    ('[{"city": "", "cp": ""}]', "Unknown, UNK00"),
    ('[{"wrong_key": "Test"}]', "Unknown, UNK00"),
    ('invalid_json', "Unknown, UNK00"),
    ('[]', "Unknown, UNK00"),
    ('null', "Unknown, UNK00")
])
def test_extract_address(json_input, expected_output):
    assert extract_address(json_input) == expected_output

# Test case for add_address_column function
def test_add_address_column():
    data = {
        "order_id": [1, 2, 3],
        "contact_data": [
            '[{"city": "Paris", "cp": "75001"}]',
            '[{"city": "Berlin", "cp": ""}]',
            '[{"city": "", "cp": "10115"}]'
        ]
    }
    df = pd.DataFrame(data)

    result_df = add_address_column(df)

    expected_data = {
        "order_id": [1, 2, 3],
        "contact_address": ["Paris, 75001", "Berlin, UNK00", "Unknown, 10115"]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df, expected_df)

