from flask import Flask, render_template
import pandas as pd
from visualizer import generate_all_plots

app = Flask(__name__)

# Load sample data
DATA_PATH = 'data/jkca_sample_data.csv'

# Load and clean data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.fillna(0)  # handle missing values
    df['Runs'] = df['Runs'].astype(int)
    df['Wickets'] = df['Wickets'].astype(int)
    return df

@app.route('/')
def index():
    df = load_data()
    
    # Generate visual insights
    generate_all_plots(df)
    
    # Select top 11 players based on performance (e.g., total runs + wickets)
    df['Performance'] = df['Runs'] + df['Wickets'] * 20  # weighted metric
    top_players = df.sort_values(by='Performance', ascending=False).head(11)

    # Convert to list of dicts for rendering in HTML
    players = top_players[['Player_Name', 'Role', 'Runs', 'Wickets']].to_dict(orient='records')
    
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)
