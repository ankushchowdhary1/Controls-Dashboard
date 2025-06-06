import streamlit as st
import pandas as pd
import plotly.express as px
from html2image import Html2Image

# Streamlit setup
st.set_page_config(layout="wide")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 6  
- **Compliant**: 4  
- **Partially Compliant**: 1  
- **Not Compliant**: 1  
""")

# Recommendations
st.markdown("""
### ✅ Recommendation
> Focus on strengthening post-implementation assurance.
> - Implement verification of control functionality after changes go live.
> - Integrate testing mechanisms into change workflows.
> - Improve documentation for prohibitive controls and audit support.
""")

# Control data
data = {
    "Control Description": [
        "Change management program", "Prohibition of changes", "Test, validate, and document changes",
        "Security impact analysis for changes", "Stakeholder notification of changes", "Control functionality verification"
    ],
    "Status": [
        "Compliant", "Partially compliant", "Compliant",
        "Compliant", "Compliant", "Not compliant"
    ],
    "Risk Rating": ["High"] * 6
}
df = pd.DataFrame(data)

# Display control table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Optional PNG export
st.subheader("📤 Export One-Pager to Image")
if st.button("Generate PNG"):
    hti = Html2Image()
    hti.screenshot(html_file="page.html", save_as="change_mgmt_summary.png")
    with open("change_mgmt_summary.png", "rb") as f:
        st.download_button("Download PNG", data=f, file_name="change_mgmt_summary.png", mime="image/png")
