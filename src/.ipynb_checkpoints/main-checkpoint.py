import pandas as pd
import json
from pathlib import Path

# Main function
def main():
    # Paths to input files
    orders_file = Path("data/orders.csv")
    invoicing_file = Path("data/invoicing_data.json")
    
    # Load data
    orders_df= load_csv(orders_file, ';')
    invoices_df = load_json(invoicing_file)

    # Test 1 - Distribution of Crate Type per Company
    crate_distribution = calculate_crate_distribution(orders_df)
    print("First rows of crate type distribution per company:")
    print(crate_distribution.head())
    
    # Test 2 - DataFrame with Full Name of the Contact
    
    # Apply the function to create a dataframe with full name and order_id columns
    df1 = add_full_name_column(orders_df)
    print("\nFirst rows of the dataFrame with Full Contact Name:")
    print(df1.head())

    # Test 3 - DataFrame with Contact Address
    # Apply the function to create a dataframe with adress and order_id columns
    df2 = add_address_column(orders_df)
    print("\nFirst rows of the dataFrame with address:")
    print(df2.head())

    #Test 4 - Sales Team Commissions
    net_comission_df = net_comissions(invoices_df)
    owners_df = ownership_categories(orders_df)
    result4_df = calculate_commissions(owners_df, net_comission_df)
    print("\nFirst rows of the dataFrame with Sales Owners Comissions:")
    print(result4_df.head())
    
    # Step 6: Test 5 - Companies with Sales Owners
    df3 = get_companies_with_salesowners(orders_df)
    print("\nFirst rows of companies with Sales Owners:")
    print(df3.head())

# Store results
    df_to_csv(crate_distribution, "Test1_CrateDistribution")
    df_to_csv(df1, "Test2_ContactFullName")
    df_to_csv(df2, "Test3_ContactAddress")
    df_to_csv(result4_df, "Test4_SalesOwnersComissions")
    df_to_csv(df3, "Test5_CompaniesSalesOwners")

############################################################ FUNCTIONS

# Function to load CSV data
def load_csv(file_path, delimiter):
    try:
        return pd.read_csv(file_path, delimiter=";")
    except Exception as e:
        print(f"Error loading CSV file {file_path}: {e}")
        return None

# Function to load JSON data
def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            invoicing_data = json.load(f)
        invoices = invoicing_data['data']['invoices']
        # invoices_df = pd.DataFrame(invoices)
        return pd.DataFrame(invoices)
    except Exception as e:
        print(f"Error loading JSON file {file_path}: {e}")
        return None

# Function to store dataframes in a csv
def df_to_csv(df, file_name):
    file_path = Path(f"results/{file_name}.csv")
    df.to_csv(file_path, index = False)
    
# Function to calculate crate distribution (Test 1)
def calculate_crate_distribution(orders_df):
    # orders_df = pd.DataFrame(data)
    # Group by company_id and crate_type, then calculate order count
    result = orders_df.groupby(["company_id","crate_type"]).size().reset_index(name="count_orders").sort_values(by="count_orders", ascending=False)
    return result

# Function to add full name column (Test 2)
def extract_full_name(json_string):
    """
    Extracts the contact_full_name from a JSON with contact information. In case this information is not available, name will be "John Doe".
    input: column with json value
    output: colum with string value
    """
    try:
        # Parse JSON string
        contact_list = json.loads(json_string)
        contact = contact_list[0]  # Is the only element in the list
        first_name = contact["contact_name"]
        last_name = contact["contact_surname"]
        
        # Combine name and surname, if full name not available then "John Doe"
        if first_name and last_name: 
            return f"{first_name} {last_name}"
        else:
            return "John Doe"
    # Adding exeption in case the format of the value is not the same as in the example
    except (json.JSONDecodeError, IndexError, KeyError, TypeError):
        return "John Doe" 
        
def add_full_name_column(orders_df):
    """
    Creates a dataframe (df_1) containing the following columns:
    order_id: Unique identifier of the order.
    contact_full_name: Full name of the contact. In case this information is not available, name will be "John Doe".
    Input: Data frame with order_id and contact_data attributes.
    Otput: Data frame with order_id and contact_data attributes.
    """
    orders_df["contact_full_name"] = orders_df["contact_data"].apply(extract_full_name)
    df_1 = orders_df[['order_id','contact_full_name']].copy()
    return df_1

# Function to add contact address column (Test 3)
def extract_address(json_string):
    """
    Extracts the contact adress from a JSON with contact information. In case this information is not available, default values of Unknown(city) and UNK00(pc).
    input: column with json value
    output: colum with string value
    """
    try:
        # Parse JSON string
        contact_list = json.loads(json_string)
        contact = contact_list[0]  # Is the only element in the list
        city_name = contact["city"]
        postal_code = contact["cp"]
        
        # Combine city and pc
        if city_name and postal_code: 
            return f"{city_name}, {postal_code}"
        elif city_name:
            return f"{city_name}, UNK00"
        elif postal_code:
            return f"Unknown, {postal_code}"
        else:
            return "Unknown, UNK00"
    # Adding exeption in case the format of the value is not the same as in the example
    except (json.JSONDecodeError, IndexError, KeyError, TypeError):
        return "Unknown, UNK00"
        
def add_address_column(orders_df):
    """
    Creates a dataframe (df_2) containing the following columns:
    order_id: Unique identifier of the order.
    contact_adress: Full name of the contact. In case this information is not available, name will be "John Doe".
    Input: Data frame with order_id and contact_data attributes.
    Otput: Data frame with order_id and contact_data attributes.
    """
    orders_df["contact_address"] = orders_df["contact_data"].apply(extract_address)
    df_2 = orders_df[['order_id','contact_address']].copy()
    return df_2

# Function to calculate sales team commissions (Test 4)
def net_comissions(invoices_df):
    """
    Creates a dataframe containing the following columns:
    order_id: Unique identifier of the order.
    netValue: contains the name of the saler with the respective ownership
    The order id atribute name is also modifyed to have the same ame as the order id column in the orders dataframe.
    Input: Data frame with orderid, grossValue and vat attributes.
    Otput: Data frame with order_id and netValue.
    """
    try: 
        invoices_df["grossValue"] = pd.to_numeric(invoices_df["grossValue"])/100
        invoices_df["vat"] = pd.to_numeric(invoices_df["vat"])
        invoices_df["netValue"] = invoices_df["grossValue"]*(1-invoices_df["vat"]*0.01)
        invoices_df["netValue"] = invoices_df["netValue"].round(2)
        invoices_df.rename(columns={"orderId":"order_id"}, inplace = True)
        return invoices_df[["order_id","netValue"]]
    except Exception as e:
        print(f"Error calculating net comission: {e}")
        return None
# Desagregate the owners column in 4 distintc category columns (main, co-1, co-2, others)
def ownership_categories(orders_df):
    """
    Creates a dataframe containing the following columns:
    order_id: Unique identifier of the order.
    main, co1 and co2: contains the name of the saler with the respective ownership
    If none saler with that level of ownership is find, column is empty.
    Input: Data frame with order_id and salesowners attributes.
    Otput: Data frame with order_id and main, co1 and co2.
    """
    try:
        owners_df = orders_df[["order_id","salesowners"]].copy()
        owners_df[["main", "co1", "co2", "rest"]] = owners_df["salesowners"].str.split(',', n=3, expand=True)
        owners_df[["main", "co1", "co2"]] = owners_df[["main", "co1", "co2"]].apply(lambda x: x.str.strip())
        return owners_df[["order_id","main","co1","co2"]]
    except Exception as e:
        print(f"Error desagregating ownership: {e}")
        return None

# Compute comissions for each level
def assign_comission(row):
    if row["ownership"] == "main":
        return row["netValue"]*0.06
    elif row["ownership"] == "co1":
        return row["netValue"]*0.025
    else:
        return row["netValue"]*0.0095
            
def calculate_commissions(owners_df, invoices_df):
    try:
        comission_df = pd.merge(owners_df, invoices_df, on = "order_id", how = "inner")
        pivoted_df = pd.melt(comission_df, id_vars = "netValue",
                         value_vars=["main", "co1", "co2"],
                         var_name="ownership",
                         value_name="salesOwner")
        # remove rows with missing any level of co-owners associted
        filtered_df = pivoted_df[pivoted_df['salesOwner'].notnull()].copy()
        filtered_df["comission"] =  filtered_df.apply(assign_comission, axis = 1)
        return filtered_df.groupby("salesOwner")["comission"].sum().round(2).sort_values(ascending=False).reset_index()
    except Exception as e:
        print(f"Error calculating comissions: {e}")
        return None

# Function to get companies with sales owners (Test 5)
def get_companies_with_salesowners(workers_df):
    try:
        # Replace NaN with empty strings to avoid split errors
        workers_df["salesowners"] = workers_df["salesowners"].fillna("")

        df = workers_df.groupby(["company_id", "company_name"])["salesowners"].agg(
            lambda x: sorted(set(
                item.strip() for sublist in x if sublist for item in sublist.split(',')
            ))
        ).reset_index()
        return df
    except Exception as e:
        print(f"Error calculating comissions: {e}")
        return None

if __name__ == "__main__":
    main()
