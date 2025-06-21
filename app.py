from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("wildfire_model.pkl")  # Make sure the model file is in the same folder

# Input features expected by the model
feature_names = ['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    if request.method == 'POST':
        try:
            # Get input values from the form
            input_data = [float(request.form[f]) for f in feature_names]
            input_df = pd.DataFrame([input_data], columns=feature_names)

            # Make prediction
            prediction = model.predict(input_df)[0]
            label = "🔥 High Risk" if prediction == 1 else "✅ Low Risk"
            prediction_text = f"Wildfire Risk: {label}"
        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    return render_template('index.html', fields=feature_names, prediction_text=prediction_text)


if __name__ == '__main__':
    app.run(debug=True)
