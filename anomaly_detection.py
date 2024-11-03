import pandas as pd
from sklearn.ensemble import IsolationForest
import logging

def detect_anomalies(df):
    """Detect anomalies in production data."""
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['production_time', 'downtime', 'resource_cost']])
    anomalies = df[df['anomaly'] == -1]
    logging.info(f"Anomalies detected: {len(anomalies)}")
    return anomalies