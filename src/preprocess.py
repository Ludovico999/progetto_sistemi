import os
import sys
import pandas as pd
import sqlite3
import numpy as np
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

def preprocess_data(selected_features):    
    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Read a table into a Pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {config.RAW_TABLE}", conn)

    # Apply preprocessing

    # Verifica che le colonne selezionate siano tutte presenti nel dataframe
    missing_cols = [col for col in selected_features if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Le seguenti colonne sono mancanti nel DataFrame: {', '.join(missing_cols)}")

    selected_columns = selected_features + ['price']
    df = df[selected_columns]

    # Save the processed data back to SQLite
    df.to_sql(config.PROCESSED_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    print(f'Dati preprocessati e caricati nella tabella {config.PROCESSED_TABLE}.')
