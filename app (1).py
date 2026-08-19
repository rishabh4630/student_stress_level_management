import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_stress_model.pkl")
scaler = joblib.load("scaler.pk1")

st.title("Student Stress Level Prediction")
st.write("Enter the student's details below to predict the stress level.")

student_type = st.selectbox(
    "Student Type",
    ["School", "College", "Working_Student"]
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=12.0,
    value=7.0
)

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=15.0,
    value=4.0
)

social_media = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    max_value=15.0,
    value=2.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

exam_pressure = st.slider("Exam Pressure", 1, 10, 5)
family_support = st.slider("Family Support", 1, 10, 5)

student_type_map = {
    "School": 0,
    "College": 1,
    "Working_Student": 2
}

student_type = student_type_map[student_type]

if st.button("Predict"):
    new_student = pd.DataFrame({
        "Student_Type": [student_type],
        "Sleep_Hours": [sleep_hours],
        "Study_Hours": [study_hours],
        "Social_Media_Hours": [social_media],
        "Attendance": [attendance],
        "Exam_Pressure": [exam_pressure],
        "Family_Support": [family_support]
    })

    new_student_scaled = scaler.transform(new_student)
    prediction = model.predict(new_student_scaled)
    probability = model.predict_proba(new_student_scaled)

    if prediction[0] == 1:
        st.success("Prediction : High Stress")
    else:
        st.success("Prediction : Low Stress")