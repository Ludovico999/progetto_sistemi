import sqlite3
import pandas as pd
import sqlite3
import pandas as pd
import logging
from src import config

import os
import src

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data():
    logging.info('Opening Excel Files...')
    df = pd.read_excel(os.path.join(config.RAW_DATA_PATH, 'Real estate valuation data set.xlsx'))

    # Rename columns
    df = df.rename(columns={
        "X5 latitude": "latitude",
        "X6 longitude": "longitude",
        "X2 house age": "house_age",
        "X1 transaction date": "transaction_date",
        "X3 distance to the nearest MRT station": "distance_MRT_station",
        "X4 number of convenience stores": "number_of_convenience_stores",
        "Y house price of unit area": "price"
    })

    # Drop unnecessary columns
    df = df.drop(columns=['transaction date', 'No'], errors='ignore')

    # Create connection to SQLite
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Write data to SQLite database
    df.to_sql(config.RAW_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    logging.info(f"Data successfully written to {config.RAW_TABLE} table.")
