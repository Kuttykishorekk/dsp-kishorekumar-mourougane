# inference.py

import pandas as pd
import joblib
import numpy as np


# Define your scale and encode columns here.
SCALE_COLS = ['GrLivArea', 'LotArea']
ENCODE_COLS = ['Neighborhood', 'MSZoning']


def make_predictions(input_data: pd.DataFrame) -> np.ndarray:
    path = '/home/kutty/Desktop/github project/dsp-kishorekumar-mourougane'
    # Loading model artifacts
    model = joblib.load(path + '/models/model.joblib')
    encoder = joblib.load(path + '/models/encoder.joblib')
    scaler = joblib.load(path + '/models/scaler.joblib')

    # Using the same features as training
    features = ["GrLivArea", "LotArea", "Neighborhood", "MSZoning"]
    encode_cols = ["Neighborhood", "MSZoning"]
    scale_cols = ["GrLivArea", "LotArea"]

    # Select the features
    input_data_selected = input_data[features].dropna(subset=encode_cols)

    # Preprocessing for new data
    input_data_encoded = encoder.transform(input_data_selected[encode_cols])
    input_data_scaled = scaler.transform(input_data_selected[scale_cols])

    # Concat scaled and encoded dataframes
    input_data_prepared = np.hstack((input_data_scaled, input_data_encoded))

    # Predicting the house prices for the new unseen data
    y_pred = model.predict(input_data_prepared)
    return y_pred
