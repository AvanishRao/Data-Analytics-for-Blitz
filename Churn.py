import pandas as pd
import numpy as np




df = pd.read_csv('Blitz.csv')

df['Date'] = pd.to_datetime(df['Date'])


df['Time In'] = df['Time In'].astype(str)
df['Time Out'] = df['Time Out'].astype(str)


df['Time In'] = pd.to_datetime(df['Date'].dt.date.astype(str) + ' ' + df['Time In'])
df['Time Out'] = pd.to_datetime(df['Date'].dt.date.astype(str) + ' ' + df['Time Out'])


df['Duration (hours)'] = (df['Time Out'] - df['Time In']).dt.total_seconds() / 3600

# Ensure 'Amount Spent (INR)' is numeric
df['Amount Spent (INR)'] = pd.to_numeric(df['Amount Spent (INR)'], errors='coerce')

# Drop rows with missing or invalid values if necessary
df.dropna(inplace=True)

# Display cleaned data
df.head()
