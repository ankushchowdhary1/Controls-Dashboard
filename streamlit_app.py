import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(layout="wide")
st.title("🔐 Identification & Access Management (IAM) — 42 Controls")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 42  
- **Compliant**: 24  
- **Not Compliant / No Response**: 15  
- **Not Assessed (NA)**: 3  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> IAM program must close ownership gaps and back claims with control evidence.
> - Assign accountability for IAM across lifecycle: creation, privilege, audit, and deletion.
> - Confirm tooling coverage (Okta, NAC, RBAC) against each control.
> - Replace NA with documented justification or roadmap actions.
""")

# Table Data (truncated for illustration; assume continuation to include all 42 rows)
data = {
    "Control Description": [
        "IAM controls implementation", "Authenticate, authorize, and audit",
        "Identification and authentication for devices", "User provisioning and deprovisioning",
        "Termination of employment", "Role-based access control", "Password-based authentication",
        "Access enforcement", "Use of privileged utility programs", "Session lock"
    ],
    "Status": [
        "No response", "No response", "Compliant", "Compliant", "Compliant",
        "Compliant", "Compliant", "Compliant", "Not compliant", "Compliant"
    ],
    "Risk Rating": ["High"] * 10
}
df = pd.DataFrame(data)

# Table Display
st.subheader("📋 Sample IAM Control Compliance Table")
st.dataframe(df, use_container_width=True, height=600)

# Export Note
st.subheader("📤 Export One-Pager")
st.caption("Use the browser's print or PDF save option. Add `html2image` to automate PNG export.")
