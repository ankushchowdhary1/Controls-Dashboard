import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("🧰 Maintenance Controls Overview (10 Total)")

# Summary
st.markdown("""
### 📊 Control Breakdown
- **Total Controls**: 10  
- **Compliant**: 1  
- **Not Compliant**: 1  
- **Not Assessed (NA)**: 8  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> Maintenance controls require foundational implementation:
> - Assign process owners for all remote and physical maintenance activities.  
> - Configure system logs and access monitoring.  
> - Align vendor SLAs with evidence-ready documentation.
""")

# Full control data
data = {
    "Control Description": [
        "Maintenance operations", "Controlled maintenance", "Timely maintenance",
        "Prevent unauthorized removal", "Remote maintenance", "Auditing remote maintenance",
        "Remote maintenance notifications", "Remote maintenance cryptographic protection",
        "Remote maintenance disconnect verification", "Authorized maintenance personnel"
    ],
    "Status": [
        "NA", "NA", "NA",
        "NA", "NA", "Not compliant",
        "NA", "NA",
        "NA", "Compliant"
    ],
    "Risk Rating": ["High"] * 10,
    "Notes": [
        "Have no evidence.",
        "Have no evidence.",
        "They keep spare parts and have vendor SLAs.",
        "Have no evidence.",
        "Have no evidence.",
        "Not aware of such activity/process.",
        "Have no evidence.",
        "Have no evidence.",
        "Have no evidence.",
        "Keep a list of DCAccess – employees and contacts."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show full table
st.subheader("📋 Full Maintenance Control Table")
st.dataframe(df, use_container_width=True, height=450)

# Export option
st.subheader("📤 Export View")
st.caption("Use browser print/PDF or integrate html2image for PNG export.")
