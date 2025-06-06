import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("🛠️ Secure Engineering, Architecture & Operations Controls")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 12  
- **Compliant**: 6  
- **Not Compliant / No Response**: 6  
""")

# Recommendations
st.markdown("""
### ✅ Recommendations
> Secure Engineering and Security Operations show mixed maturity:
> - Formalize architectural alignment, centralized control management, and time sync enforcement.  
> - Validate and enforce standard notification banners and truncated warnings.  
> - Integrate operations processes into broader control monitoring and reporting lifecycle.
""")

# Control Table Data
data = {
    "Control Description": [
        "Secure engineering principles",
        "Centralized management of cybersecurity and data privacy controls",
        "Alignment with enterprise architecture",
        "Technical debt reviews",
        "Defense in depth architecture",
        "Non-persistence",
        "System use notification (logon banner)",
        "Standardized Microsoft Windows banner",
        "Truncated banner",
        "Clock synchronization",
        "Standardized operating procedures (SOP)",
        "Security Concept of Operations"
    ],
    "Risk Rating": ["High"] * 12,
    "Status": [
        "Compliant", "Not Compliant", "Not Compliant", "Compliant", "Not Compliant",
        "Compliant", "Not Compliant", "Compliant", "Not Compliant", "Not Compliant",
        "Compliant", "Not Compliant"
    ]
}

# Display table
st.subheader("📋 Control Table")
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True, height=550)

# Export
st.subheader("📤 Export View")
st.caption("Use browser print/save to PDF or integrate with html2image for PNG export.")
