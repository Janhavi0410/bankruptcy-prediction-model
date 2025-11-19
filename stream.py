import pickle
import numpy as np
import pandas as pd
import streamlit as st
import pyperclip

# Load trained model
model_path = "random_forest_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Define selected features
SELECTED_FEATURES = ['X8', 'X15', 'X3', 'X1', 'X17', 'X7', 'X13', 'X10', 'X14', 'X6']
COLUMN_NAMES = [
    "Debt Ratio", "Net Income", "ROA", "Total Assets", "Short-Term Debt",
    "Revenue Growth", "Operating Cash Flow", "Total Liabilities",
    "Working Capital", "Current Ratio"
]

# Initialize session state for inputs
if "inputs" not in st.session_state:
    st.session_state.inputs = {feature: 0.0 for feature in SELECTED_FEATURES}

# Streamlit UI
st.title("Bankruptcy Prediction App")
st.write("Enter financial features to predict company status")

# Create input table
data = {"Feature": COLUMN_NAMES, "Value": [st.session_state.inputs[feature] for feature in SELECTED_FEATURES]}
df = pd.DataFrame(data)

edited_df = st.data_editor(df, num_rows="fixed")

# Update session state with new values
for i, feature in enumerate(SELECTED_FEATURES):
    st.session_state.inputs[feature] = edited_df.iloc[i, 1]

# Function to predict
def predict():
    try:
        values = [st.session_state.inputs[feature] for feature in SELECTED_FEATURES]
        input_df = pd.DataFrame([values], columns=SELECTED_FEATURES)
        prediction = model.predict(input_df)[0]
        return "Company is Alive" if prediction == 1 else "Company can Fail"
    except Exception as e:
        return "Error"

# Predict button
if st.button("Predict"):
    prediction = predict()
    if prediction == "Company is Alive":
        st.success(f"{prediction}")
    else:
        st.error(f"{prediction}")

# Auto-fill from clipboard
if st.button("Fill Inputs from Clipboard"):
    try:
        clipboard_data = pyperclip.paste()
        values = clipboard_data.split()
        if len(values) == len(SELECTED_FEATURES):
            for i, feature in enumerate(SELECTED_FEATURES):
                st.session_state.inputs[feature] = float(values[i])
            st.rerun()
        else:
            st.error(f"Expected {len(SELECTED_FEATURES)} values, got {len(values)}.")
    except Exception as e:
        st.error("Failed to read clipboard data.")