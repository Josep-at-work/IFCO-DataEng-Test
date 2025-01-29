# IFCO Technical Test

## Environment Configuration
1. Clone this repo
2. Create a python virtual environemnt
   ```bash
   python -m venv <venv>
   source <venv>/bin/activate
3. Install dependencies
```bash
   python install -r requirements.txt

## Execute the main module
In the root directory of the project in you terminal activate the environment and execute the main.py
```bash
   source <venv>/bin/activate
(venv) python src/main.py

This will print the first rows of the 4 dataframes as well as save the whole dataframe in the respective results file located in the results directory

## Exexute tests
Again in the root directory, activate the environment (skip this step if it's already done). Then execute the tests with pytest
```bash
   source <venv>/bin/activate
(venv) python src/main.py
   pytest tests/
