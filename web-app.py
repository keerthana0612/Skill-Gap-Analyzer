import streamlit as st
import pandas as pd
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("🎓 AI Skill Gap Analyzer")

st.write("Enter your skill levels (1 to 10)")

python = st.slider("Python",1,10)
ml = st.slider("Machine Learning",1,10)
communication = st.slider("Communication",1,10)
sql = st.slider("SQL",1,10)
statistics = st.slider("Statistics",1,10)
cloud = st.slider("Cloud",1,10)

input_data = pd.DataFrame([[python, ml, communication, sql, statistics, cloud]],
columns=["Python","ML","Communication","SQL","Statistics","Cloud"])

if st.button("Analyze Career Path"):

    prediction = model.predict(input_data)

    if prediction[0] == "Technical":

        st.success("You are suitable for TECHNICAL roles 🚀👨‍💻")

        st.subheader("📜 Possible Technical Roles")

        st.write("""
        - Software Developer
        - Data Scientist
        - AI Engineer
        - Machine Learning Engineer
        - Cloud Engineer
        - DevOps Engineer
        - Cyber Security Analyst
        - Database Administrator
        - Full Stack Developer
        - Backend Developer
        - Frontend Developer
        - Mobile App Developer
        - Game Developer
        - System Engineer
        - Network Engineer
        """)

        st.subheader("📈 Skill Improvement Suggestions")

        if python < 7:
            st.write("🔹 Improve Python")
        if ml < 7:
            st.write("🔹 Improve Machine Learning")
        if communication < 7:
            st.write("🔹 Improve Communication")
        if sql < 7:
            st.write("🔹 Improve SQL")
        if statistics < 7:
            st.write("🔹 Improve Statistics")
        if cloud < 7:
            st.write("🔹 Improve Cloud")

    else:

        st.success("You are suitable for NON-TECHNICAL roles 🎯")

        st.subheader("📜 Possible Non-Technical Roles")

        st.write("""
        - HR Manager
        - Marketing Executive
        - Business Analyst
        - Project Manager
        - Product Manager
        - Sales Manager
        - Operations Manager
        - Digital Marketing Specialist
        - Customer Success Manager
        - Content Strategist
        - Social Media Manager
        - Public Relations Officer
        - Event Manager
        - Entrepreneur
        - Training Officer
        """)

        st.subheader("📈 Skill Improvement Suggestions")

        st.write("🔹 Improve Leadership")
        st.write("🔹 Improve Presentation Skills")
        st.write("🔹 Improve Decision Making")

        st.write("🔹 Improve Communication")
