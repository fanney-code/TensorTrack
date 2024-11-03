import pandas as pd
from fpdf import FPDF
from analysis import show_summary
import logging

def generate_report(user_profile, df, report_path):
    """Generate a PDF report based on user profile and analysis."""
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, 'Industrial Efficiency Report', ln=True, align='C')
    pdf.cell(0, 10, '', ln=True)  # Empty line

    # Company Information
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, f"Company Name: {user_profile['company_name']}", ln=True)
    pdf.cell(0, 10, f"Address: {user_profile['address']}", ln=True)
    pdf.cell(0, 10, '', ln=True)  # Empty line

    # Analysis Results
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, 'Analysis Results', ln=True)

    diminished_productivity, escalated_expenditures, compromised_profitability = show_summary(df)

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Diminished Productivity: {diminished_productivity:.2f}", ln=True)
    pdf.cell(0, 10, f"Escalated Expenditures: {escalated_expenditures:.2f}", ln=True)
    pdf.cell(0, 10, f"Compromised Profitability: {compromised_profitability:.2f}", ln=True)

    # Save the PDF
    pdf.output(report_path)