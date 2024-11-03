import customtkinter as ctk
from flask import Flask, request, jsonify, render_template
import pandas as pd
import logging
from data_handler import load_data, clean_data
from analysis import analyze_productivity, show_summary
from anomaly_detection import detect_anomalies
from forecasting import train_forecasting_model, forecast_costs
from report_generator import generate_report
from ai_model import ProductionPredictor
import os
import json

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No file selected.'}), 400
    df = load_data(file)
    if df is None:
        return jsonify({'message': 'Error loading data.'}), 500
    df = clean_data(df)
    return jsonify({'message': 'File uploaded successfully.', 'total_records': len(df)})

@app.route('/report')
def report():
    # Generate report logic
    return jsonify({'message': 'Report generated successfully.'})

@app.route('/download_report')
def download_report():
    # Logic to download the generated report
    return jsonify({'message': 'Report downloaded successfully.'})

@app.route('/last_chart_info')
def last_chart_info():
    # Logic to fetch last uploaded data
    return jsonify({'key': 'value'})  # Replace with actual data

if __name__ == "__main__":
    app.run(debug=True)