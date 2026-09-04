import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("⚡ Energy Load Prediction App")
st.markdown("Model yordamida energiya yuklamasini bashorat qilish")

# basic inputlar
col1, col2 = st.columns(2)

with col1:
    hour = st.number_input("Hour", 0, 23)
    month = st.number_input("Month", 1, 12)

with col2:
    day = st.number_input("Day", 1, 31)
    usage = st.number_input("Usage_kWh")

# qo‘shimcha inputlar
week = st.selectbox("WeekStatus", ["Weekday", "Weekend"])
day_name = st.selectbox("Day of week", [
    "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
])

if st.button("Predict"):
    data = np.zeros((1, 17))

    # asosiy featurelar
    data[0][0] = usage
    data[0][7] = hour
    data[0][8] = month
    data[0][9] = day

    # WeekStatus
    data[0][6] = 0 if week == "Weekday" else 1

    # Day of week (one-hot)
    days = ["Friday","Monday","Saturday","Sunday","Thursday","Tuesday","Wednesday"]
    idx = days.index(day_name)
    data[0][10 + idx] = 1

    result = model.predict(data)
    st.success(f"Prediction: {result[0]}")
