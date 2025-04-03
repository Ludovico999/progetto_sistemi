from src import config
import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import os
import sys
import pickle
import logging

sys.path.append(os.path.abspath(".."))  # Adds the parent directory to sys.path

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT latitude, longitude, house_age, distance_MRT_station, number_of_convenience_stores, price FROM housing_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_model():
    """Trains a Random Forest model using all available features and saves it."""
    
    df = load_data()

    # Divide features and target
    X = df.drop(columns=['price'])
    y = df['price']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Save model
    with open(os.path.join(config.MODELS_PATH, "random_forest_regressor.pickle"), "wb") as file:
        pickle.dump(model, file)

    # Save evaluation metrics
    from sklearn.metrics import mean_absolute_error, r2_score
    y_pred = model.predict(X_test)
    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "R2": r2_score(y_test, y_pred),
    }

    conn = sqlite3.connect(config.DATABASE_PATH)
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(config.EVALUATION_TABLE, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    logging.info("Model trained and saved successfully.")




