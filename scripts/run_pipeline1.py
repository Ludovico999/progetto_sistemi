import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
from src import config
from src.load_data import load_data
from src.preprocess import preprocess_data
from src.make_model import train_model

# Set up logging
logging.basicConfig(filename='../logs/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting Pipeline previsione immobiliare")

    # Step 1: Load data from Excel and store it in SQLite
    logging.info("Loading raw data...")
    load_data()

    # Step 2: Preprocess data con tutte le feature disponibili
    #logging.info("Preprocessing data...")
    #preprocess_data(['latitude', 'longitude', 'house_age', 'distance_MRT_station', 'number_of_convenience_stores'])


    train_model()

    logging.info("Pipeline completata con successo.")

if __name__ == "__main__":
    main()
