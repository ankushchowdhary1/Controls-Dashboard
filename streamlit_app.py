import streamlit as st
import pandas as pd
import plotly.express as px
from html2image import Html2Image
import os

# Data
data = {
    "Control Description": [
        "Asset governance", "Asset inventories", "Data action mapping",
        "Network diagrams & data flow diagrams", "Unattended end user equipment",
        "Tamper detection", "Secure disposal", "Use of third party devices",
        "BYOD", "Prohibited equipment & services", "Asset categorization"
    ],
    "Status": [
        "Compliant", "Compliant", "Not compliant", "Partially compliant",
        "Compliant", "Compliant", "Compliant", "Compliant",
        "Not compliant", "Not compliant", "Not compliant"
    ],
    "Risk Rating": ["High"] * 11
}
df = pd.DataFrame(data)

# Summary
st.set_page_config(layout="wide")
st.title("🔍 Asset Management (12 Controls) Overview")

st.markdown("""
### 📊 Summary
- **Total Controls**: 12  
- **Compliant**: 6  
- **Partially Compliant**: 1  
- **Not Compliant**: 5  
""")

# Recommendations
st.markdown("""
### ✅ Recommendation
> Prioritize remediation of missing processes and visibility gaps:
> - Formalize asset categorization, mapping, and prohibited services documentation.
> - Audit BYOD usage and enforce formal controls.
> - Use existing Axonius system to drive automation and monitoring.
""")

# Show Table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Export section
st.subheader("📤 Export One-Pager to Image")
if st.button("Generate PNG"):
    hti = Html2Image()
    hti.screenshot(html_file="page.html", save_as="asset_mgmt_summary.png")
    with open("asset_mgmt_summary.png", "rb") as f:
        st.download_button("Download PNG", data=f, file_name="asset_mgmt_summary.png", mime="image/png")
