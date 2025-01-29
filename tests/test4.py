import pytest
import pandas as pd
from main import net_comissions, ownership_categories, calculate_commissions

@pytest.fixture
def sample_invoices_df():
    """Fixture to create a sample invoices dataframe"""
    data = {
        "orderId": ["ORD1", "ORD2", "ORD3"],
        "grossValue": ["10000", "20000", "15000"],  # Values in cents
        "vat": ["10", "20", "15"]  # VAT in percentage
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_orders_df():
    """Fixture to create a sample orders dataframe"""
    data = {
        "order_id": ["ORD1", "ORD2", "ORD3"],
        "salesowners": ["Alice, Bob", "Charlie, David, Eve", "Frank"]
    }
    return pd.DataFrame(data)

def test_net_comissions(sample_invoices_df):
    """Test net_comissions function"""
    result = net_comissions(sample_invoices_df)
    
    expected_data = {
        "order_id": ["ORD1", "ORD2", "ORD3"],
        "netValue": [90.00, 160.00, 127.50]  # Expected net values
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result, expected_df)

def test_ownership_categories(sample_orders_df):
    """Test ownership_categories function"""
    result = ownership_categories(sample_orders_df)
    
    expected_data = {
        "order_id": ["ORD1", "ORD2", "ORD3"],
        "main": ["Alice", "Charlie", "Frank"],
        "co1": ["Bob", "David", None],
        "co2": [None, "Eve", None]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result, expected_df)

def test_calculate_commissions(sample_orders_df, sample_invoices_df):
    """Test calculate_commissions function"""
    owners_df = ownership_categories(sample_orders_df)
    invoices_df = net_comissions(sample_invoices_df)
    result = calculate_commissions(owners_df, invoices_df)

    expected_data = {
        "salesOwner": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
        "comission": [5.40, 2.25, 9.60, 4.00, 1.52, 7.65]  # Expected commissions
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result, expected_df)

