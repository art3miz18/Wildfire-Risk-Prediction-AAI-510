import streamlit as st
import joblib
import pandas as pd

# Load trained model
st.set_page_config(
    page_title="Wildfire Risk Predictor",
    page_icon="🔥",
    layout="centered",
)


@st.cache_resource
def load_model():
    """Load and cache the trained model."""
    return joblib.load("wildfire_model.pkl")


model = load_model()

# Input features expected by the model
FEATURES = ['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']

def main():
    st.title("🔥 Wildfire Risk Predictor")
    st.write("Enter the environmental conditions below to estimate the chance of a wildfire.")

    with st.form("prediction_form"):
        cols = st.columns(4)
        user_input = {}
        for i, feature in enumerate(FEATURES):
            user_input[feature] = cols[i % 4].number_input(feature, value=0.0, step=0.1)
        submitted = st.form_submit_button("Predict")

    if submitted:
        input_df = pd.DataFrame([user_input])
        prediction = model.predict(input_df)[0]
        label = "High Risk" if prediction == 1 else "Low Risk"
        if prediction == 1:
            st.error(f"Wildfire Risk: 🔥 {label}")
        else:
            st.success(f"Wildfire Risk: ✅ {label}")

if __name__ == "__main__":
    main()
