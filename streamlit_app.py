import streamlit as st
import pandas as pd

# Streamlit setup
st.set_page_config(layout="wide")
st.title("🔐 IAM Controls Overview – Grouped by Category")

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
> IAM program must close ownership and evidence gaps.  
> - Assign ownership per category (e.g., PAM, Provisioning, Enforcement).  
> - Verify control implementation vs. assumptions (e.g., system defaults).  
> - Add audit-ready evidence for all compliant and NA-rated controls.
""")

# Grouped data
groups = {
    "Authentication & Authorization": [
        "IAM controls implementation", "Authenticate, authorize, and audit", "Multi-factor authentication",
        "Password-based authentication", "Replay-resistant authentication", "Authenticator management",
        "PKI-based authentication", "Session lock", "Session termination"
    ],
    "User Lifecycle Management": [
        "User provisioning and deprovisioning", "Change of roles and duties", "Termination of employment",
        "Management approval for new or changed accounts", "Identity proofing/verification",
        "Identifier management (user names)", "User Identity Management"
    ],
    "Privileged Access Management (PAM)": [
        "Network access to privileged accounts", "Privileged access by non-organizational users",
        "Privileged account management (PAM)", "Privileged account identifiers", "Privileged accounts",
        "Use of privileged utility programs", "Access to sensitive/regulated data"
    ],
    "Access Control Enforcement": [
        "Role-based access control", "Access enforcement", "Disable inactive accounts",
        "Revocation of access authorization", "Account lockout",
        "Prohibit non-privileged users from executing privileged functions", "Least privilege",
        "Authorize access to security functions"
    ],
    "Activity & Evidence Monitoring": [
        "Auditing use of privileged functions", "Periodic review of account privileges", "System account reviews",
        "Anomalous behavior", "No embedded unencrypted static authenticators",
        "Hardware token-based authentication", "In-person or trusted third party registration"
    ],
    "Shared Credentials & Exceptions": [
        "Restrictions on shared groups/accounts", "Credentials sharing", "Database access",
        "Vendor-supplied defaults", "Account disabling for high-risk individuals",
        "Non-privileged access for non-security functions"
    ]
}

# Mock status data (for illustration)
data = {
    "Control Description": [],
    "Category": [],
    "Status": [],
    "Risk Rating": []
}

status_map = {
    "Compliant": 24,
    "Not compliant / No response": 15,
    "NA": 3
}

# Assign statuses to mimic realistic control spread
import itertools
statuses = list(itertools.chain(
    ["Compliant"] * 24,
    ["Not compliant / No response"] * 15,
    ["NA"] * 3
))

i = 0
for group, controls in groups.items():
    for control in controls:
        data["Control Description"].append(control)
        data["Category"].append(group)
        data["Status"].append(statuses[i] if i < len(statuses) else "Compliant")
        data["Risk Rating"].append("High")
        i += 1

# DataFrame
df = pd.DataFrame(data)

# Display grouped tables
for category in groups.keys():
    st.subheader(f"📁 {category}")
    st.dataframe(df[df["Category"] == category], use_container_width=True, height=400)

# Export option
st.subheader("📤 Export One-Pager")
st.caption("Use the browser's print or PDF save option. Add html2image if PNG export is needed.")
