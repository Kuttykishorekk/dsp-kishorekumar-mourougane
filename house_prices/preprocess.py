from sklearn.preprocessing import StandardScaler, OneHotEncoder


def preprocess(dataframe):
    # Select Features
    features = ['GrLivArea', 'LotArea', 'Neighborhood', 'MSZoning']
    targeted_feature = ['SalePrice']
    df_selected = dataframe[features + targeted_feature]
    # Clean Missing Values
    df_selected = df_selected.dropna()
    # Define columns for scaling/encoding
    scale_cols = ['GrLivArea', 'LotArea']
    encode_cols = ['Neighborhood', 'MSZoning']

    # Initialize Encoder and Scaler
    scaler = StandardScaler()
    encoder = OneHotEncoder(drop='first', sparse=False)

    # Fit and transform
    scaler.fit(df_selected[scale_cols])
    encoder.fit(df_selected[encode_cols])
    return scaler, encoder, scale_cols, encode_cols
