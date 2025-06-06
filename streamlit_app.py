import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("🛡️ Compliance (6 Controls) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 6  
- **Compliant**: 1  
- **Partially Compliant**: 2  
- **Not Compliant**: 3  
""")

# Recommendations
st.markdown("""
### ✅ Recommendation
> Prioritize governance and regulatory traceability.
> - Assign ownership for compliance and cybersecurity regulation coverage.
> - Implement routine assessments for data protection and governmental access handling.
> - Leverage existing ISO 27001/9001 certification to build missing documentation.
""")

# Control data
data = {
    "Control Description": [
        "Statutory, regulatory and contractual controls identification",
        "Non-compliance oversight",
        "Compliance scope",
        "Cybersecurity & data protection controls oversight",
        "Cybersecurity & data protection assessment",
        "Government surveillance"
    ],
    "Status": [
        "Compliant", "Not compliant", "Partially compliant",
        "Partially compliant", "Not compliant", "Not compliant"
    ],
    "Risk Rating": ["High"] * 6
}
df = pd.DataFrame(data)

# Table display
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Export note
st.subheader("📤 Export One-Pager")
st.caption("Use your browser’s print/save to PDF option or integrate with html2image for automation.")
