import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import logging

class ProductionPredictor:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.is_trained = False

    def train_predictive_maintenance_model(self, df):
        """Train the predictive maintenance model."""
        try:
            X = df[['usage_hours', 'last_maintenance']]
            y = df['maintenance_needed']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train)
            self.is_trained = True
            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            logging.info(f"Predictive maintenance model trained with accuracy: {accuracy:.2f}")
        except Exception as e:
            logging.error(f"Error training predictive maintenance model: {e}")

    def predict_maintenance(self, usage_hours, last_maintenance):
        """Predict if maintenance is needed based on usage hours and last maintenance date."""
        if not self.is_trained:
            raise Exception("Model has not been trained yet.")
        prediction = self.model.predict([[usage_hours, last_maintenance]])
        return prediction[0]