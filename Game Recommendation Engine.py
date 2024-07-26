import gradio as gr
import pandas as pd

# Load the dataset
steam_data = pd.read_csv('steam2.csv', header=None)
steam_data.columns = ['user_id', 'game', 'action', 'value', 'other']

# Filter only purchase actions
steam_data_purchase = steam_data[steam_data['action'] == 'purchase']

# Define a simple recommendation function
def recommend(user_id, num_recommendations):
    user_id = int(user_id)
    num_recommendations = int(num_recommendations)

    # Get the games the user has purchased
    purchased_games = steam_data_purchase[steam_data_purchase['user_id'] == user_id]['game'].unique().tolist()

    # Get the most popular games that the user hasn't purchased
    popular_games = steam_data_purchase['game'].value_counts().index.tolist()
    recommendations = [game for game in popular_games if game not in purchased_games][:num_recommendations]

    return ", ".join(recommendations)

# Create the Gradio interface
iface = gr.Interface(
    fn=recommend,
    inputs=[
        gr.components.Number(label="User ID"),
        gr.components.Number(label="Number of Recommendations")
    ],
    outputs=gr.components.Textbox(label="Recommended Games"),
    title="Game Recommendation System",
    description="Enter your user ID and the desired number of recommendations to get personalized game recommendations."
)

# Launch the interface
iface.launch(share=True)
