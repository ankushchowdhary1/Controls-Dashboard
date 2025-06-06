import streamlit as st
import pandas as pd

# Page setup
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
> Formalize monitoring ownership and evidence gathering:
> - Align teams (IR, Infra, Compliance) with specific controls.
> - Validate systems like QRadar, NTP sync, and log correlation tooling.
> - Replace NA labels with documented evaluations or action plans.
""")

# Data
data = {
    "Control Description": [
        "Continuous monitoring controls", "Intrusion detection and prevention systems", "Automated tools for real-time analysis",
        "Inbound and outbound communications traffic", "File integrity monitoring (FIM)", "Log reviews and updates",
        "Centralized collection of security event logs", "Correlate monitoring information", "Audit trails", "Time stamps",
        "Protection of event logs", "Event log retention", "Anomalous behavior"
    ],
    "Status": [
        "Partially compliant", "Partially compliant", "NA", "Not compliant", "Not compliant", "NA",
        "NA", "Not compliant", "Not compliant", "Compliant", "NA", "Compliant", "NA"
    ],
    "Risk Rating": ["High"] * 13
}
df = pd.DataFrame(data)

# Table Display
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True, height=700)

# Export section
st.subheader("📤 Export One-Pager")
st.caption("Use the browser's print or PDF save option. Or use html2image for automation.")
