# IFCO Technical Test

## Project directories

**Notebooks:**
   - Data Exploration: loading two datasets and checking the attributes
   - Scenarios: Load the data and process all transformations: Test1, Test2, Test3, Test4, and Test5.
   - Test 6 visualization: Answer the 3 questions proposed for the visualizations part.


**SRC:**
   - main.py: Script to execute Test1, Test2, Test3, Test4 and Test5 transformations, described in the problem statement.

**Test:**  
   - Testing scripts for the processes/transformation done in test1, tes2, test3 and test5, described in the problem statement.

## Execution
The following steps describe how to execute the project from a windows CMD.

### Environment Configuration
1. Clone this repo
2. Create a python virtual environemnt
   ```bash
   python -m venv <venv>
   ```
3. Activate and install dependencies
```bash
   <venv>\Scripts\activate
   uv pip install -r requirements.txt
```
### Execute the main module
In the root directory of the project in your terminal activate the environment and execute the main.py
```bash
   <venv>\Scripts\activate
   python src/main.py
```
This will print the first rows of the 4 dataframes as well as save the whole dataframe in the respective results file located in the results directory

### Execute tests
Again in the root directory, activate the environment (skip this step if it's already done). Then execute the tests with pytest, for example test1
```bash
   <venv>\Scripts\activate
   (venv) pytest tests/test1
```
Each test is for a different transformation. 

The following is a summary of the problem statements:

You have been assigned the responsibility of assisting IFCO's Data Team in the analysis of some business data. For this purpose, you have been provided with two files:

orders.csv (which contains factual information regarding the orders received)
invoicing_data.json (which contains invoicing information)

- Test 1: Distribution of Crate Type per Company. Calculate the distribution of crate types per company (number of orders per type). Ensure to include unit tests to validate the correctness of your calculations.

- Test 2: DataFrame of Orders with Full Name of the Contact. Provide a DataFrame (df_1) containing the following columns:

order_id:	The order_id field must contain the unique identifier of the order.
contact_full_name:	The contact_full_name field must contain the full name of the contact. In case this information is not available, the placeholder "John Doe" should be utilized.

- Test 3: DataFrame of Orders with Contact Address. Provide a DataFrame (df_2) containing the following columns:

order_id:	The order_id field must contain the unique identifier of the order.
contact_address:	The field for contact_address should adhere to the following information and format: "city name, postal code". In the event that the city name is not available, the placeholder "Unknown" should be used. Similarly, if the postal code is not known, the placeholder "UNK00" should be used.

- Test 4: Calculation of Sales Team Commissions . The Sales Team requires your assistance in computing the commissions. It is possible for multiple salespersons to be associated with a single order, as they may have participated in different stages of the order. The salesowners field comprises a ranked list of the salespeople who have ownership of the order. The first individual on the list represents the primary owner, while the subsequent individuals, if any, are considered co-owners who have contributed to the acquisition process. The calculation of commissions follows a specific procedure:

Main Owner: 6% of the net invoiced value.
Co-owner 1 (second in the list): 2.5% of the net invoiced value.
Co-owner 2 (third in the list): 0.95% of the net invoiced value.
The rest of the co-owners do not receive anything.
Provide a list of the distinct sales owners and their respective commission earnings. The list should be sorted in order of descending performance, with the sales owners who have generated the highest commissions appearing first.

- Test 5: DataFrame of Companies with Sales Owners. Provide a DataFrame (df_3) containing the following columns:

company_id	The company_id field must contain the unique identifier of the company.
company_name	The company_name field must contain the name of the company.
list_salesowners	The list_salesowners field should contain a unique and comma-separated list of salespeople who have participated in at least one order of the company. Please ensure that the list is sorted in ascending alphabetical order of the first name.

- Test 6: Data Visualization (you don't need to submit a solution to this test if not explicitly asked for)
The Sales team wants to understand which sales owners are particularly successful in creating orders in plastic crates. Create a set of appropriate visualizations / reports that help your stakeholders to understand the following aspects better:

1. What is the distribtion of orders by crate type.
2. Which sales owners need most training to improve selling on plastic crates, based on the last 12 months orders.
3. Understand who are by month the top 5 performers selling plastic crates for a rolling 3 months evaluation window.
