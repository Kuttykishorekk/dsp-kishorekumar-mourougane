
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from joblib import dump
import numpy as np


def build_model(data: pd.DataFrame) -> dict:
    # Feature Selection
    features = ["GrLivArea", "LotArea",
                "Neighborhood", "MSZoning"]
    target = ["SalePrice"]

    # Split data into train and test sets
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Encoding and Scaling Initialization
    encode_cols = ["Neighborhood", "MSZoning"]
    encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
    scale_cols = ["GrLivArea", "LotArea"]
    scaler = StandardScaler()

    # Encoding categorical columns
    encoder.fit(X_train[encode_cols])
    X_train_encoded = encoder.transform(X_train[encode_cols])
    X_test_encoded = encoder.transform(X_test[encode_cols])

    # Scaling numerical columns
    scaler.fit(X_train[scale_cols])
    X_train_scaled = scaler.transform(X_train[scale_cols])
    X_test_scaled = scaler.transform(X_test[scale_cols])

    # Concatenating the scaled and encoded variables
    X_train_prepared = np.hstack((X_train_scaled, X_train_encoded))
    X = np.hstack((X_test_scaled, X_test_encoded))

    # Train the model
    model = LinearRegression()
    model.fit(X_train_prepared, y_train)
    path = '/home/kutty/Desktop/github project/dsp-kishorekumar-mourougane'

    dump(model, path + '/models/model.joblib')
    dump(encoder, path + '/models/encoder.joblib')
    dump(scaler, path + '/models/scaler.joblib')

    return {"message": "Model has been successfully trained and saved."}
