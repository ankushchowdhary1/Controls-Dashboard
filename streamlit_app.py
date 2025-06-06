import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("📡 Continuous Monitoring (14 Controls) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 14  
- **Compliant**: 1  
- **Partially Compliant**: 2  
- **Not Compliant**: 5  
- **Not Assessed (NA)**: 6  
""")

# Recommendations
st.markdown("""
### ✅ Recommendation
> This domain requires urgent visibility and structure.
> - Assign control ownership across teams (IR, Infra, Security).
> - Audit configuration of logs, file monitoring, IDS/IPS systems.
> - Remove “NA” status by clarifying team responsibilities and validating deployment status.
""")

# Table data
data = {
    "Control Description": [
        "Continuous monitoring controls", "Intrusion detection and prevention systems",
        "Automated tools for real-time analysis", "Inbound and outbound communications traffic",
        "File integrity monitoring (FIM)", "Log reviews and updates",
        "Centralized collection of security event logs", "Correlate monitoring information",
        "Audit trails", "Time stamps"
    ],
    "Status": [
        "Partially compliant", "Partially compliant", "NA", "Not compliant",
        "Not compliant", "NA", "NA", "Not compliant",
        "Not compliant", "Compliant"
    ],
    "Risk Rating": ["High"] * 10
}
df = pd.DataFrame(data)

# Display table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Export section
st.subheader("📤 Export One-Pager")
st.caption("Use your browser’s print or PDF save feature for now. PNG automation optional via `html2image`.")
