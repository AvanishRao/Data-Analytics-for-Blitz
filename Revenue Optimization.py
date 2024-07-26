import pandas as pd
from collections import Counter

# Load the data from the CSV file
data = pd.read_csv("Blitz.csv")

# Calculate total revenue
total_revenue = data["Amount Spent (INR)"].sum()
print(f"Total Revenue: {total_revenue:.2f} INR")

# Analyze revenue by game
revenue_by_game = data.groupby("Game Played ")["Amount Spent (INR)"].sum().sort_values(ascending=False)
most_profitable_games = revenue_by_game.index.tolist()[:3]
print(f"\nMost Profitable Games: {', '.join(most_profitable_games)}")

# Identify the most popular games
game_counts = Counter(data["Game Played "])
popular_games = [game for game, count in game_counts.most_common(3)]
print(f"\nMost Popular Games: {', '.join(popular_games)}")

# Analyze revenue by time of day
data["Time In"] = pd.to_datetime(data["Time In"], format="%H:%M")
data["Hour"] = data["Time In"].dt.hour
hourly_revenue = data.groupby("Hour")["Amount Spent (INR)"].sum().sort_index()
peak_hours = hourly_revenue[hourly_revenue >= hourly_revenue.quantile(0.75)].index.tolist()
print(f"\nPeak Hours: {', '.join(map(str, peak_hours))}")

# Analyze revenue by PC
revenue_by_pc = data.groupby("PC Used")["Amount Spent (INR)"].sum().sort_values(ascending=False)
most_profitable_pcs = revenue_by_pc.index.tolist()[:3]
print(f"\nMost Profitable PCs: {', '.join(most_profitable_pcs)}")

# Identify the most popular PCs
pc_counts = Counter(data["PC Used"])
popular_pcs = [pc for pc, count in pc_counts.most_common(3)]
print(f"\nMost Popular PCs: {', '.join(popular_pcs)}")

# Analyze customer loyalty
customer_visits = data.groupby("Customer ID").size().sort_values(ascending=False)
loyal_customers = customer_visits[customer_visits >= customer_visits.quantile(0.75)].index.tolist()
print(f"\nNumber of Loyal Customers (top 25%): {len(loyal_customers)}")

# Promotional strategies
print("\nPromotional Strategies:")
print("1. Focus on the most popular and profitable games:")
print(", ".join(set(most_profitable_games + popular_games)))

print("\n2. Offer special promotions, tournaments, or events during peak hours:")
for hour in peak_hours:
    print(f"- {hour}:00 - {hour+1}:00")

print("\n3. Ensure the most popular and profitable PCs are well-maintained and readily available:")
print(", ".join(set(most_profitable_pcs + popular_pcs)))

print("\n4. Implement loyalty programs or rewards for loyal customers.")

# Analyze revenue by game genre
genres = {
    "League of Legends": "MOBA",
    "Dota 2": "MOBA",
    "Fortnite": "Battle Royale",
    "Apex Legends": "Battle Royale",
    "Call of Duty": "FPS",
    "CS2": "FPS",
    "Valorant": "FPS",
    "Elden Ring": "RPG",
    "Far Cry": "FPS",
    "Brawlhalla": "Fighting",
    "Minecraft": "Sandbox",
    "Rocket League": "Sports",
    "PUBG": "Battle Royale"
}

data["Genre"] = data["Game Played "].map(genres)
revenue_by_genre = data.groupby("Genre")["Amount Spent (INR)"].sum().sort_values(ascending=False)
print("\nRevenue by Genre:")
print(revenue_by_genre)

# Potential new games based on popular genres
potential_new_games = []
for genre, revenue in revenue_by_genre.items():
    if genre in ["MOBA", "Battle Royale", "FPS", "RPG"]:
        potential_new_games.extend([f"New {genre} Game 1", f"New {genre} Game 2"])

print(f"\nPotential New Games to Introduce: {', '.join(potential_new_games)}")

# Adjust pricing strategies
print("\nAdjust pricing strategies based on demand and popularity:")
for game in most_profitable_games + popular_games:
    print(f"- Increase price for {game} during peak hours")

for pc in most_profitable_pcs + popular_pcs:
    print(f"- Increase price for {pc} during peak hours")
