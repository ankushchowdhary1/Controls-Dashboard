import streamlit as st
import pandas as pd

# Streamlit setup
st.set_page_config(layout="wide")
st.title("☁️ Cloud Security (4 Controls) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 4  
- **Compliant**: 1  
- **Partially Compliant**: 1  
- **Not Compliant**: 2  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> Establish formal cloud security controls:
> - Introduce cloud-specific policy ownership.
> - Enforce visibility over API usage and multi-tenant environments.
> - Validate built-in provider security with internal evidence or attestations.
""")

# Data
data = {
    "Control Description": [
        "Cloud services controls implementation", "API security",
        "Multi-tenant environments governance", 
        "Geolocation requirements for processing, storage, and service locations"
    ],
    "Status": ["Partially compliant", "Not compliant", "Not compliant", "Compliant"],
    "Risk Rating": ["High"] * 4
}
df = pd.DataFrame(data)

# Table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Optional export
st.subheader("📤 Export One-Pager")
st.caption("To download as PNG, use browser’s print feature (Save as Image/PDF) or integrate `html2image` for automation.")
