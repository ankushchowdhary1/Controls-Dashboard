import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("🧰 Maintenance Controls Overview (10 Total)")

# Summary Section
st.markdown("""
### 📊 Summary
- **Total Controls**: 10  
- **Compliant**: 1  
- **Not Compliant**: 9  
- **NA values interpreted as Not Compliant due to lack of evidence**
""")

# Recommendations Section
st.markdown("""
### ✅ Recommendations
> The maintenance domain exhibits significant control implementation gaps:
> - Assign formal ownership for maintenance policy, execution, and tracking.  
> - Implement controls for remote maintenance protections, notifications, cryptography, and access authorization.  
> - Ensure alignment of service vendors with internal control expectations and document SLAs.
""")

# Control Table Data
data = {
    "Control Description": [
        "Maintenance operations",
        "Controlled maintenance",
        "Timely maintenance",
        "Prevent unauthorized removal",
        "Remote maintenance",
        "Auditing remote maintenance",
        "Remote maintenance notifications",
        "Remote maintenance cryptographic protection",
        "Remote maintenance disconnect verification",
        "Authorized maintenance personnel"
    ],
    "Risk Rating": ["High"] * 10,
    "Status": [
        "Not Compliant", "Not Compliant", "Not Compliant",
        "Not Compliant", "Not Compliant", "Not Compliant",
        "Not Compliant", "Not Compliant", "Not Compliant", "Compliant"
    ]
}

# DataFrame and display
df = pd.DataFrame(data)

st.subheader("📋 Maintenance Controls Table")
st.dataframe(df, use_container_width=True, height=450)

# Export option
st.subheader("📤 Export One-Pager")
st.caption("Use your browser's print or PDF export. For PNG, integrate html2image.")
