import pandas as pd
import logging

def analyze_productivity(df):
    """Analyze productivity and identify bottlenecks."""
    df['efficiency'] = df['production_time'] / (df['production_time'] + df['downtime'])
    bottlenecks = df[df['downtime'] > df['downtime'].mean() + df['downtime'].std()]
    logging.info("Bottlenecks identified.")
    return df, bottlenecks

def show_summary(df):
    """Calculate and show summary metrics to help users understand the data better."""
    diminished_productivity = df['production_time'].sum() / (df['production_time'].sum() + df['downtime'].sum())
    escalated_expenditures = df['resource_cost'].sum() * 1.1
    compromised_profitability = df['resource_cost'].sum() - df['production_time'].sum() * 10

    logging.info("Calculated metrics: Diminished Productivity, Escalated Expenditures, Compromised Profitability.")
    return diminished_productivity, escalated_expenditures, compromised_profitability