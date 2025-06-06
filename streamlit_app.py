import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("🧩 Configuration Management (10 Controls) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 10 (+2 NA)  
- **Compliant**: 4  
- **Partially Compliant**: 1  
- **Not Compliant**: 4  
- **Not Assessed (NA)**: 2  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> Establish formal baseline documentation and strengthen configuration visibility.
> - Assign ownership for system hardening and tailoring controls.
> - Audit user-install permissions and clarify open-source usage policies.
> - Expand process awareness and evidence collection for NA areas.
""")

# Control Data
data = {
    "Control Description": [
        "Configuration management", "System hardening through baseline configurations", "Respond to unauthorized changes",
        "Approved configuration deviations", "Baseline tailoring", "Least functionality", "Software usage restrictions",
        "Open source software", "User-installed software", "Restrict roles permitted to install software"
    ],
    "Status": [
        "Not compliant", "Not compliant", "Compliant", "Compliant", "Not compliant", "Partially compliant",
        "Compliant", "NA", "Compliant", "NA"
    ],
    "Risk Rating": ["High"] * 10
}
df = pd.DataFrame(data)

# Table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True)

# Export Note
st.subheader("📤 Export One-Pager")
st.caption("Use your browser’s print/save option or integrate with html2image for image export.")
