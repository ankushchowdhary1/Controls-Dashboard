import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("🧰 Maintenance Controls Overview (10 Total)")

# Summary Section
st.markdown("""
### 📊 Control Breakdown
- **Total Controls**: 10  
- **Compliant**: 1  
- **Not Compliant**: 1  
- **Not Assessed (NA)**: 8  

The majority of maintenance controls are currently not assessed (NA), indicating a gap in ownership or process documentation. Only one control is compliant, and one is explicitly marked as non-compliant.
""")

# Recommendation Section
st.markdown("""
### ✅ Recommendation
> Maintenance domain requires foundational process design and documentation:
> - Assign a responsible team or owner for maintenance governance.  
> - Formalize remote maintenance procedures, notifications, and cryptographic safeguards.  
> - Ensure audit logging, disconnect verification, and access restrictions are verifiable.  
> - Review SLAs with vendors to include compliance with internal control expectations.
""")

# Control Table Data
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
        "They keep some spare parts to replace in case of a malfunction. In addition, they have support and service agreements with vendors to replace parts within agreed SLA.",
        "Have no evidence.",
        "Have no evidence.",
        "Not aware of such activity/process.",
        "Have no evidence.",
        "Have no evidence.",
        "Have no evidence.",
        "Keep a list of DCAccess – a list of employees and their contact information."
    ]
}

# Create and display DataFrame
df = pd.DataFrame(data)

st.subheader("📋 Maintenance Control Table")
st.dataframe(df, use_container_width=True, height=500)

# Export Option
st.subheader("📤 Export View")
st.caption("Use browser print/PDF or integrate html2image for PNG export.")
