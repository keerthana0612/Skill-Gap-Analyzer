import streamlit as st
import pandas as pd
import pickle
import os

# Set page config FIRST (before any other streamlit commands)
st.set_page_config(page_title="AI Skill Gap Analyzer")

# Load model properly (for cloud also)
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("🎓 AI Skill Gap Analyzer")

st.write("Analyze whether you are suitable for Technical or Non-Technical career path")

st.subheader("Enter Your Skill Levels (1 to 10)")

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
        - IoT Engineer
        - Data Engineer
        - Automation Engineer
        - Robotics Engineer
        - Web Developer
        """
        )

        st.subheader("📈 Skills You Should Improve")

        if python < 7:
            st.warning("🔹 Improve Python")
        if ml < 7:
            st.warning("🔹 Improve Machine Learning")
        if communication < 7:
            st.warning("🔹 Improve Communication")
        if sql < 7:
            st.warning("🔹 Improve SQL")
        if statistics < 7:
            st.warning("🔹 Improve Statistics")
        if cloud < 7:
            st.warning("🔹 Improve Cloud")

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
        - Talent Acquisition Specialist
        - Brand Manager
        - Business Development Executive
        - Client Relationship Manager
        - Startup Founder
        """
        )

        st.subheader("📈 Skills You Should Improve")

        if communication < 7:
            st.warning("🔹 Improve Communication")
        st.warning("🔹 Improve Leadership")
        st.warning("🔹 Improve Decision Making")
        st.warning("🔹 Improve Presentation Skills")
        st.warning("🔹 Improve Team Management")
