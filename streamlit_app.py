import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("📡 Continuous Monitoring (14 Controls) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 14  
- **Compliant**: 2  
- **Partially Compliant**: 2  
- **Not Compliant**: 5  
- **Not Assessed (NA)**: 5  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> Consolidate tooling and ownership for detection and monitoring controls.
> - Align SIEM (QRadar) and IR ownership with compliance reporting.
> - Clarify responsibility for FIM, audit trails, anomaly detection, and centralized logging.
> - Convert NA-rated controls into either compliant or non-compliant with documented evaluations.
""")

# Control Data
data = {
    "Control Description": [
        "Continuous monitoring controls", "Intrusion detection and prevention systems",
        "Automated tools for real-time analysis", "Inbound and outbound communications traffic",
        "File integrity monitoring (FIM)", "Log reviews and updates",
        "Centralized collection of security event logs", "Correlate monitoring information",
        "Audit trails", "Time stamps",
        "Protection of event logs", "Event log retention", "Anomalous behavior"
    ],
    "Status": [
        "Partially compliant", "Partially compliant", "NA", "Not compliant",
        "Not compliant", "NA", "NA", "Not compliant",
        "Not compliant", "Compliant",
        "NA", "Compliant", "NA"
    ],
    "Risk Rating": ["High"] * 13
}
df = pd.DataFrame(data)

# Table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Export option
st.subheader("📤 Export One-Pager")
st.caption("Use browser print/save or integrate html2image for automation.")
