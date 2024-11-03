import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import logging

def train_forecasting_model(df):
    """Train a forecasting model using linear regression."""
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].map(pd.Timestamp.timestamp)
    X = df[['date', 'production_time', 'downtime']]
    y = df['resource_cost']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    logging.info(f"Model trained with R^2 score: {score:.2f}")
    return model

def forecast_costs(model, future_dates):
    """Forecast future costs based on the model."""
    future_data = np.array([[pd.Timestamp(date).timestamp(), 50, 5] for date in future_dates])
    predictions = model.predict(future_data)
    return predictions