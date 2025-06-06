import streamlit as st
import pandas as pd

# Streamlit setup
st.set_page_config(layout="wide")
st.title("🔐 IAM Control Summary by Category")

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
> Focus IAM improvement on ownership clarity and evidence collection.
> - Assign leads per control category.
> - Verify claims with tooling coverage (e.g., Okta, NAC).
> - Transition NA to verified compliant or gap-documented.
""")

# Group definitions
groups = {
    "Authentication & Authorization": 9,
    "User Lifecycle Management": 7,
    "Privileged Access Management (PAM)": 7,
    "Access Control Enforcement": 8,
    "Activity & Evidence Monitoring": 7,
    "Shared Credentials & Exceptions": 4
}

# Status assignment (mocked for summary)
status_counts = {
    "Authentication & Authorization": {"Compliant": 5, "Not Compliant": 3, "NA": 1},
    "User Lifecycle Management": {"Compliant": 5, "Not Compliant": 2, "NA": 0},
    "Privileged Access Management (PAM)": {"Compliant": 4, "Not Compliant": 2, "NA": 1},
    "Access Control Enforcement": {"Compliant": 5, "Not Compliant": 2, "NA": 1},
    "Activity & Evidence Monitoring": {"Compliant": 3, "Not Compliant": 3, "NA": 1},
    "Shared Credentials & Exceptions": {"Compliant": 2, "Not Compliant": 3, "NA": 0}
}

# Display table summary
data = []
for category, total in groups.items():
    comp = status_counts[category]["Compliant"]
    nc = status_counts[category]["Not Compliant"]
    na = status_counts[category]["NA"]
    data.append({
        "Category": category,
        "Total Controls": total,
        "Compliant": comp,
        "Not Compliant": nc,
        "NA": na
    })

summary_df = pd.DataFrame(data)
st.subheader("📋 IAM Grouped Control Summary")
st.dataframe(summary_df, use_container_width=True, height=400)

# Export section
st.subheader("📤 Export Summary")
st.caption("Use the browser's print or PDF save option. Add html2image if PNG export is needed.")
