from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

app = Flask(__name__)

# Load model and encoders
model = tf.keras.models.load_model("ipl_score_predictor.h5")
scaler = joblib.load("scaler.pkl")
venue_encoder = joblib.load("venue_encoder.pkl")
batting_team_encoder = joblib.load("batting_team_encoder.pkl")
bowling_team_encoder = joblib.load("bowling_team_encoder.pkl")
striker_encoder = joblib.load("striker_encoder.pkl")
bowler_encoder = joblib.load("bowler_encoder.pkl")

# Load data for dropdowns
ipl = pd.read_csv("ipl_data.csv")
df = ipl.drop(['date', 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5','mid', 'striker', 'non-striker'], axis=1)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html",
        venues=df['venue'].unique(),
        batting_teams=df['bat_team'].unique(),
        bowling_teams=df['bowl_team'].unique(),
        batsmen=df['batsman'].unique(),
        bowlers=df['bowler'].unique()
    )

@app.route('/predict', methods=['POST'])
def predict():
    venue = request.form['venue']
    bat_team = request.form['bat_team']
    bowl_team = request.form['bowl_team']
    batsman = request.form['batsman']
    bowler = request.form['bowler']

    venue = venue_encoder.transform([venue])[0]
    bat_team = batting_team_encoder.transform([bat_team])[0]
    bowl_team = bowling_team_encoder.transform([bowl_team])[0]
    batsman = striker_encoder.transform([batsman])[0]
    bowler = bowler_encoder.transform([bowler])[0]

    input_data = np.array([[venue, bat_team, bowl_team, batsman, bowler]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)[0][0]

    return render_template("index.html",
        venues=df['venue'].unique(),
        batting_teams=df['bat_team'].unique(),
        bowling_teams=df['bowl_team'].unique(),
        batsmen=df['batsman'].unique(),
        bowlers=df['bowler'].unique(),
        prediction=int(prediction)
    )

if __name__ == '__main__':
    app.run(debug=True)
