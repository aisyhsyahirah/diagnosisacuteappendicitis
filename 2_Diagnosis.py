import streamlit as st
import numpy as np
import pandas as pd

class DummyModel:
    def predict(self, X):
        return [1 if x[2] > 12 and x[3] > 10 else 0 for x in X]
    def predict_proba(self, X):
        return [[0.2, 0.8] if x[2] > 12 and x[3] > 10 else [0.9, 0.1] for x in X]

model = DummyModel()

st.title("🩺 Diagnosis Tool")
st.markdown("Fill in the patient's clinical data to receive an automated assessment for possible acute appendicitis.")

with st.form("diagnosis_form"):
    st.subheader("Patient Information")
    age = st.number_input("Age (years)", min_value=0, max_value=18, value=10)
    sex = st.radio("Sex", options=["Female", "Male"])
    sex_binary = 1 if sex == "Female" else 0

    st.subheader("Symptoms & Lab Results")
    migratory_pain = st.checkbox("Migratory right iliac fossa pain")
    lower_right_pain = st.checkbox("Right iliac fossa pain/tenderness")
    rebound = st.checkbox("Rebound tenderness")

    wbc = st.number_input("WBC Count (x10³/μL)", min_value=0.0, max_value=50.0, value=11.0)
    crp = st.number_input("CRP (mg/L)", min_value=0.0, max_value=300.0, value=8.0)
    neutro = st.slider("Neutrophil Percentage (%)", 0, 100, 65)

    submitted = st.form_submit_button("Run Diagnosis")

if submitted:
    st.subheader("🔍 Diagnosis Result")
    input_data = np.array([[
        age, sex_binary, wbc, crp, neutro,
        int(migratory_pain), int(lower_right_pain), int(rebound)
    ]])

    prediction = model.predict(input_data)[0]
    probas = model.predict_proba(input_data)[0]
    confidence = probas[1] * 100

    if prediction == 1:
        st.error(f"⚠️ **Likely Appendicitis** (Confidence: {confidence:.1f}%)")
        st.markdown("**Recommendation:** Urgent clinical evaluation is advised.")
    else:
        st.success(f"✅ **Appendicitis Unlikely** (Confidence: {100 - confidence:.1f}%)")
        st.markdown("**Recommendation:** Monitor symptoms. Reassess if condition worsens.")

    st.divider()
    st.markdown("🔬 **Model Decision Inputs**")
    df = pd.DataFrame(input_data, columns=[
        "Age", "Sex", "WBC", "CRP", "Neutrophils",
        "Migratory Pain", "RIF Pain", "Rebound Tenderness"
    ])
    st.dataframe(df)
