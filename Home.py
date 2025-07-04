import streamlit as st
st.set_page_config(page_title="Early Diagnosis Acute Appendicitis in Children", layout="wide")

# Main Title
st.markdown(
    """
    <h1 style="display: flex; align-items: center;">
        <span style="margin-right: 10px;">🩺</span>
        Early Diagnosis Acute Appendicitis in Children
    </h1>
    """,
    unsafe_allow_html=True
)

# Disclaimer
st.error(
    "**IMPORTANT DISCLAIMER:** This is a prototype diagnostic tool for research and educational purposes only. "
    "It is not intended for clinical use and should not replace professional medical judgment. Always consult "
    "with qualified healthcare professionals for medical diagnosis and treatment decisions."
)

# About Section
st.markdown("## About This System")
st.markdown("""
This diagnostic assistant prototype uses machine learning to help pediatricians assess the likelihood of acute appendicitis in children. 
The system analyzes clinical parameters including symptoms, physical examination findings, and laboratory values to provide risk assessment and recommendations.
""")

# Key Features List
st.markdown("**Key Features:**")
st.markdown("""
- 📊 **Dashboard**: Overview of system performance and statistics  
- 🩺 **Diagnosis Tool**: Interactive assessment form for clinical evaluation  
- 🧠 **ML-Powered**: Advanced algorithms trained on pediatric appendicitis data  
- 📋 **Clinical Decision Support**: Evidence-based recommendations for next steps
""")


# Section Break for Next Content
st.markdown("## What is Appendicitis in Children?")
