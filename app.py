import streamlit as st
import pandas as pd
import joblib

# Load the saved model pipeline
model = joblib.load('traffic_model.pkl')

st.set_page_config(page_title="Traffic AI", page_icon="🚦")
st.title("🚦 AI Traffic Signal Optimization")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    lane = st.selectbox("Lane ID", ["North_S", "North_L", "South_S", "South_L", "East_S", "East_L", "West_S", "West_L"])
    weather = st.selectbox("Weather", ["Clear", "Rainy", "Foggy"])
    v_count = st.number_input("Vehicle Count", 0, 200, 25)
with col2:
    hour = st.slider("Hour (24h format)", 0, 23, 12)
    speed = st.slider("Avg Speed (km/h)", 5, 100, 40)
    amb = st.radio("Ambulance Present?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")

# Prediction
if st.button("Predict Green Time"):
    # Create input DataFrame (must match backend columns)
    input_df = pd.DataFrame([[hour, lane, 150, weather, v_count, speed, amb]], 
                             columns=['Hour', 'Lane_ID', 'Lane_Length_m', 'Weather', 'Vehicle_Count', 'Avg_Speed_kmh', 'Ambulance_Present'])
    
    res = model.predict(input_df)[0]
    st.success(f"Suggested Green Light Duration: {res:.2f} Seconds")