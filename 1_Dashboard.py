import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("📊 System Dashboard")

st.markdown("This dashboard provides an overview of the system's performance, usage statistics, and machine learning model results.")

# Section 1: System Usage Stats
st.header("📈 System Usage Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Patients Assessed", "1,254", "+45 this week")
col2.metric("Model Accuracy", "91.3%", "↑ 1.2%")
col3.metric("Avg. Time per Diagnosis", "1.3 mins", "-0.2 mins")

st.divider()

# Section 2: Model Performance Metrics
st.subheader("🤖 Machine Learning Model Performance")
model_metrics = {
    'Accuracy': 0.913,
    'Precision': 0.89,
    'Recall': 0.92,
    'F1 Score': 0.90,
    'AUC-ROC': 0.94
}
st.dataframe(pd.DataFrame.from_dict(model_metrics, orient='index', columns=['Score']).style.format("{:.2%}"))

# Section 3: Visualization
st.subheader("📊 Diagnosis Outcome Distribution")
outcomes = pd.DataFrame({
    "Diagnosis": ["Appendicitis", "No Appendicitis"],
    "Count": [845, 409]
})
fig, ax = plt.subplots()
ax.bar(outcomes["Diagnosis"], outcomes["Count"], color=["#ff6961", "#77dd77"])
ax.set_ylabel("Number of Cases")
ax.set_title("Total Cases Diagnosed")
st.pyplot(fig)

# Section 4: Upcoming Features
st.divider()
st.markdown("### 💡 Upcoming Features")
st.markdown("""
- Real-time data integration from hospital EHR
- Patient demographic heatmaps
- Model retraining trigger system
- Exportable diagnosis reports (PDF)
""")
