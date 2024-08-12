import os
import pandas as pd
from google.cloud import bigquery

credentials_file = "polygon-service-account.json"
if os.path.exists(credentials_file):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file

client = bigquery.Client()

def get_erc20_data():
    query = """
    SELECT *
    FROM polygon.erc20_network_raw
    WHERE partition_date = '2024-08-08'
    LIMIT 10
    """

    data = client.query(query).to_dataframe()

    return data

def get_transaction_data():
    query = """
    SELECT *
    FROM polygon.polygon_network
    WHERE partition_date = '2024-08-08'
    LIMIT 10
    """

    data = client.query(query).to_dataframe()

    return data

df_erc20_data = get_erc20_data()
df_tx_data = get_transaction_data()
print(df_erc20_data)
print(df_tx_data)


