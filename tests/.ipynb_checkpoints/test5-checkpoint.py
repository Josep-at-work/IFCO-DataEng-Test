import pytest
import pandas as pd
from main import get_companies_with_salesowners

@pytest.fixture
def sample_workers_df():
    """Fixture to create a sample workers dataframe"""
    data = {
        "company_id": [1, 1, 2, 2, 3],
        "company_name": ["Company A", "Company A", "Company B", "Company B", "Company C"],
        "salesowners": ["Alice, Bob", "Bob, Charlie", "David, Eve", "Eve, Frank", "Grace"]
    }
    return pd.DataFrame(data)

def test_get_companies_with_salesowners(sample_workers_df):
    """Test get_companies_with_salesowners function"""
    result = get_companies_with_salesowners(sample_workers_df)

    expected_data = {
        "company_id": [1, 2, 3],
        "company_name": ["Company A", "Company B", "Company C"],
        "salesowners": [["Alice", "Bob", "Charlie"], ["David", "Eve", "Frank"], ["Grace"]]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result, expected_df)

def test_empty_salesowners():
    """Test when there are empty salesowners"""
    workers_df = pd.DataFrame({
        "company_id": [1, 2],
        "company_name": ["Company A", "Company B"],
        "salesowners": ["", None]
    })

    result = get_companies_with_salesowners(workers_df)

    expected_df = pd.DataFrame({
        "company_id": [1, 2],
        "company_name": ["Company A", "Company B"],
        "salesowners": [[] for _ in range(2)]
    })

    pd.testing.assert_frame_equal(result, expected_df)

