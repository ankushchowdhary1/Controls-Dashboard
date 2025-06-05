import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Compliance Summary Dashboard", layout="wide")
st.title("🔍 Compliance Summary Overview")

# KPI values
total_controls = 227
non_relevant_controls = 52
relevant_controls = total_controls - non_relevant_controls
compliant_controls = 80
non_compliant_controls = 95

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Controls Tested", total_controls)
col2.metric("Non-Relevant Controls", non_relevant_controls)
col3.metric("Fully Compliant Controls", f"{compliant_controls} ({round(compliant_controls / relevant_controls * 100)}%)")
col4.metric("Non-Compliant Controls", f"{non_compliant_controls} ({round(non_compliant_controls / relevant_controls * 100)}%)")

# Donut Chart for Compliance Status
data = pd.DataFrame({
    "Status": ["Compliant", "Non-Compliant", "Non-Relevant"],
    "Count": [compliant_controls, non_compliant_controls, non_relevant_controls]
})

fig = px.pie(
    data,
    names='Status',
    values='Count',
    hole=0.5,
    title="Control Compliance Distribution",
    color_discrete_sequence=px.colors.qualitative.Set2
)

st.plotly_chart(fig, use_container_width=True)

# --- Domain-level breakdown table ---
st.subheader("📊 Domain-Level Control Breakdown")
domain_data = pd.DataFrame({
    "Domain": [
        "Asset Management", "Change Management", "Cloud Security", "Compliance", "Configuration Management",
        "Continuous Monitoring", "Endpoint Security", "Identification & Authentication", "Maintenance",
        "Network Security", "Physical & Environmental Security", "Secure Engineering & Architecture",
        "Security Operations", "Technology Development & Acquisition", "Vulnerability & Patch Management",
        "Web Security"
    ],
    "Total Tested": [12, 6, 4, 6, 10, 14, 12, 53, 10, 29, 14, 10, 2, 29, 12, 4],
    "Relevant": [10, 5, 2, 3, 6, 12, 11, 39, 9, 22, 14, 7, 1, 20, 10, 4],
    "Compliant %": [70, 80, 50, 33, 50, 16, 27, 44, 11, 27, 64, 57, 100, 55, 50, 100],
    "Evidence Uploaded": [1, 2, 0, 0, 1, 0, 0, 5, 1, 0, 3, 1, 0, 0, 0, 0],
    "Guidelines": [6, 3, 1, 1, 2, 2, 3, 16, 1, 6, 6, 3, 1, 11, 5, 4]
})

selected_domain = st.selectbox("Select a Domain to Highlight", ["All"] + domain_data["Domain"].tolist())
filtered_data = domain_data if selected_domain == "All" else domain_data[domain_data["Domain"] == selected_domain]
st.dataframe(filtered_data)

bar_fig = px.bar(
    filtered_data,
    x="Domain",
    y="Compliant %",
    title="Compliance Percentage by Domain",
    labels={"Compliant %": "Compliance %"},
    color="Compliant %",
    color_continuous_scale="Teal"
)
st.plotly_chart(bar_fig, use_container_width=True)
