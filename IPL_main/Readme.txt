# 🏏 IPL Score Predictor (Deep Learning + Flask Web App)

This project is a web-based machine learning application that predicts the **final score of an IPL team’s innings** based on input parameters like venue, teams, and player details. The prediction is powered by a trained **deep learning model** built using **TensorFlow/Keras** and deployed using **Flask**.

---

## 📌 Features

- Predicts total innings score of an IPL team.
- Clean Flask-based web interface with dropdown inputs.
- Real-time prediction without reloading the page.
- Encodes and scales input data dynamically before prediction.

---

## 📂 Dataset Description

- **File Used:** `ipl_data.csv`
- **Source:** Publicly available IPL ball-by-ball dataset
- **Features Used:**
  - Venue
  - Batting Team
  - Bowling Team
  - Batsman (Striker)
  - Bowler
- **Target:** `total` runs in the innings

Columns like `date`, `mid`, `striker`, `non-striker`, `runs_last_5`, `overs`, etc. were dropped to simplify the model.

---

## 🧠 Model Architecture

- Input Layer: 5 features (encoded)
- Hidden Layers:
  - Dense(512, ReLU)
  - Dense(216, ReLU)
- Output Layer: Dense(1, Linear)
- Loss Function: Huber Loss
- Optimizer: Adam
- Trained for 50 epochs with batch size 64

---

## 🔁 How It Works (Step-by-Step)

1. **User Interface:**
   - User selects input parameters via dropdowns (venue, teams, players).

2. **Backend Processing (Flask):**
   - Inputs are encoded using pre-fitted `LabelEncoders`.
   - Data is normalized using `MinMaxScaler`.
   - Encoded and scaled data is passed into the trained Keras model.

3. **Prediction:**
   - The model outputs a numerical score prediction.
   - The predicted score is rendered on the same page.

---

## ⚙️ Installation & Setup

### 1️⃣ Download the Repository


  ## Open the Project Folder in VS Code

  ## Make sure the folder contains:

	.app.py
	.ipl_data.csv
	.pkl files
	.h5 model
	.templates/ folder with index.html
	.Static/styl.css
 
### FOLDER SHOULD LOCK LIKE THIS 
	IPL_main/
	│
	├── app.py                  # Flask application
	├── ipl_data.csv            # IPL dataset
	├── scaler.pkl              # Trained MinMaxScaler
	├── venue_encoder.pkl       # Label encoder for venues
	├── batting_team_encoder.pkl
	├── bowling_team_encoder.pkl
	├── striker_encoder.pkl
	├── bowler_encoder.pkl
	├── ipl_score_predictor.h5  # Trained Keras model
	├── templates/
	│   └── index.html          # Web interface
	└── static/
	    └── style.css (optional)



  ## Open a Terminal in VS Code(RUN ONE BY ONE):
	.pip install flask
	.pip install numpy
	.pip install pandas
	.pip install scikit-learn
	.pip install tensorflow
	.pip install joblib

  ## Run the Flask App(IN TERMINAL)
	python app.py

If successful, you should see:
Running on http://127.0.0.1:5000/


EXTRA IF NOT WORK(IN TERMINAL OR CMD OF PROJECT FOLDER)
	python -m venv venv

