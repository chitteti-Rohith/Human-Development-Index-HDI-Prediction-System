#  Human Development Index - Flask Web Application
#  Run: python app.py   (after training the model first)
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("HDI.pkl", "rb"))


# ── Routes ────────────────────────────────────────────────────

@app.route("/")
@app.route("/Home", methods=["POST", "GET"])
def home():
    return render_template("home.html")


@app.route("/Prediction", methods=["POST", "GET"])
def prediction():
    return render_template("indexnew.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Read form values submitted by user
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = [
    "Country",
    "Life expectancy",
    "Mean years of schooling",
    "GNI per capita",
    "Internet users",
   ]

    df = pd.DataFrame(features_value, columns=features_name)

    # Generate prediction
    output = model.predict(df)
    y_pred = round(output[0][0], 2)

    # Classify into HDI tier
    if 0.30 <= y_pred <= 0.40:
        prediction_text = "Low HDI — " + str(y_pred)
    elif 0.40 < y_pred <= 0.70:
        prediction_text = "Medium HDI — " + str(y_pred)
    elif 0.70 < y_pred <= 0.80:
        prediction_text = "High HDI — " + str(y_pred)
    elif 0.80 < y_pred <= 0.94:
        prediction_text = "Very High HDI — " + str(y_pred)
    else:
        prediction_text = (
            "The given values do not match the expected range. "
            "Please check your inputs."
        )

    return render_template("resultnew.html", prediction_text=prediction_text)


# ── Entry Point ───────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)
