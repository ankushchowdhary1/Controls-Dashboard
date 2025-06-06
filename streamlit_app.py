import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("🛡️ Vulnerability & Patch Management Controls (12 Total)")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 12  
- **Compliant**: 5  
- **Not Compliant / No Response**: 7  
""")

# Recommendations
st.markdown("""
### ✅ Recommendations
> While core scanning and remediation using Rapid7 is well-established, automation and centralized tracking are lacking:
> - Improve visibility into patching and remediation workflow across platforms.  
> - Assign accountability for automation status, event review, and internal scans.  
> - Validate and document all control functions, especially those marked "No response".
""")

# Control Table
controls = {
    "Control Description": [
        "Vulnerability & patch management program",
        "Vulnerability remediation",
        "Software and firmware patching",
        "Centralized management of flaw remediation processes",
        "Automated remediation status",
        "Vulnerability scanning",
        "Privileged access",
        "Trend analysis",
        "Review historical event logs",
        "External vulnerability assessment scans",
        "Internal vulnerability assessment scans",
        "Penetration testing"
    ],
    "Risk Rating": ["High"] * 12,
    "Status": [
        "Compliant", "Compliant", "Not Compliant", "Not Compliant",
        "Not Compliant", "Compliant", "Not Compliant", "Compliant",
        "Not Compliant", "Compliant", "Not Compliant", "Not Compliant"
    ]
}

# Render DataFrame
st.subheader("📋 Vulnerability & Patch Control Table")
df = pd.DataFrame(controls)
st.dataframe(df, use_container_width=True, height=500)

# Export
st.subheader("📤 Export View")
st.caption("Use browser print/save. PNG export available via html2image.")
