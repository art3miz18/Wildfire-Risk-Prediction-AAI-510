import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("wildfire_model.pkl")

# Input features expected by the model
FEATURES = ['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']

def main():
    st.title("Wildfire Risk Prediction")
    st.write("Enter the weather parameters below to estimate wildfire risk.")

    # Collect user input
    user_input = {}
    for feature in FEATURES:
        user_input[feature] = st.number_input(feature, value=0.0)

    if st.button("Predict"):
        input_df = pd.DataFrame([user_input])
        prediction = model.predict(input_df)[0]
        label = "🔥 High Risk" if prediction == 1 else "✅ Low Risk"
        st.success(f"Wildfire Risk: {label}")

if __name__ == "__main__":
    main()
