import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for raw data (Excel files)
RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw/")

# SQLite Database Path
DATABASE_PATH = os.path.join(BASE_DIR, "../database/immobiliare.db")

# Preprocessed Data Table Name
PROCESSED_TABLE = "processed_housing_data"

# Raw Data Table Name
RAW_TABLE = "housing_data"

# Predictions Table Name
PREDICTIONS_TABLE = "predictions"

# model evaluation
EVALUATION_TABLE = "model_evaluation"

# Logging Configuration
LOGGING_LEVEL = "INFO"


#Saved models
MODELS_PATH = '../models/'

