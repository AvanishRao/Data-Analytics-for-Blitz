import pandas as pd
from collections import Counter

# Load the data from the CSV file
data = pd.read_csv("Blitz.csv")

# Calculate total revenue
total_revenue = data["Amount Spent (INR)"].sum()
print(f"Total Revenue: {total_revenue:.2f} INR")

# Analyze revenue by game
revenue_by_game = data.groupby("Game Played ")["Amount Spent (INR)"].sum().sort_values(ascending=False)
print("\nRevenue by Game:")
print(revenue_by_game)

# Identify the most popular games
game_counts = Counter(data["Game Played "])
popular_games = [game for game, count in game_counts.most_common(3)]
print(f"\nMost Popular Games: {', '.join(popular_games)}")

# Analyze revenue by time of day
data["Time In"] = pd.to_datetime(data["Time In"], format="%H:%M")
data["Hour"] = data["Time In"].dt.hour
hourly_revenue = data.groupby("Hour")["Amount Spent (INR)"].sum().sort_index()
print("\nHourly Revenue:")
print(hourly_revenue)

# Identify peak hours
peak_hours = hourly_revenue[hourly_revenue >= hourly_revenue.quantile(0.75)].index.tolist()
print(f"\nPeak Hours: {', '.join(map(str, peak_hours))}")

# Analyze revenue by PC
revenue_by_pc = data.groupby("PC Used")["Amount Spent (INR)"].sum().sort_values(ascending=False)
print("\nRevenue by PC:")
print(revenue_by_pc)

# Identify the most popular PCs
pc_counts = Counter(data["PC Used"])
popular_pcs = [pc for pc, count in pc_counts.most_common(3)]
print(f"\nMost Popular PCs: {', '.join(popular_pcs)}")

# Analyze customer loyalty
customer_visits = data.groupby("Customer ID").size().sort_values(ascending=False)
loyal_customers = customer_visits[customer_visits >= customer_visits.quantile(0.75)].index.tolist()
print(f"\nNumber of Loyal Customers (top 25%): {len(loyal_customers)}")
