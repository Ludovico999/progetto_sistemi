import os
import sys
import numpy as np
sys.path.append(os.path.abspath(".."))
from src import config
import streamlit as st
import pickle
import pandas as pd

# Carica il modello
with open(os.path.join(config.MODELS_PATH, "random_forest_regressor.pickle"), "rb") as file:
    model = pickle.load(file)

# Titolo dell'applicazione
st.title("Previsione Prezzo Immobiliare")

# Opzione di selezione per le variabili
selected_vars = st.selectbox(
    "Seleziona le variabili per la previsione del prezzo della casa:",
    ("Latitudine e Longitudine", 'Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze')
)

# Input per le feature scelte
input_data = {}

if selected_vars == "Latitudine e Longitudine":
    latitudine = input_data["latitude"] = st.number_input("Inserisci la latitudine:")
    longitudine = input_data["longitude"] = st.number_input("Inserisci la longitudine:")
elif selected_vars == 'Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze':
    eta = input_data["house_age"] = st.number_input("Inserisci l'età della casa:")
    distance = input_data["distance_MRT_station"] = st.number_input("Distanza alla stazione MRT:")
    num_stores = input_data["number_of_convenience_stores"] = st.number_input("Numero di negozi di convenienza:")
else:
    latitudine = input_data["latitude"] = st.number_input("Inserisci la latitudine:")
    longitudine = input_data["longitude"] = st.number_input("Inserisci la longitudine:")
    eta = input_data["house_age"] = st.number_input("Inserisci l'età della casa:")
    distance = input_data["distance_MRT_station"] = st.number_input("Distanza alla stazione MRT:")
    num_stores = input_data["number_of_convenience_stores"] = st.number_input("Numero di negozi di convenienza:")

# Predizione quando il bottone viene cliccato
if st.button("Predici"):
    if selected_vars == "Latitudine e Longitudine":
        x_input = np.array([[latitudine, longitudine, 17, 1083, 4]])
        prediction = model.predict(x_input)[0]
    elif selected_vars == 'Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze':
        x_input = np.array([[25, 121, eta, distance, num_stores]])
        prediction = model.predict(x_input)[0]      
    st.success(f"Il prezzo previsto della casa è: {round(prediction, 2)} dollari per unità di area")
