import streamlit as st
import pandas as pd

# Page config
st.set_page_config(layout="wide")
st.title("🌐 Network Security Controls Overview (29 Total)")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 29  
- **Compliant**: 6  
- **Not Compliant / No Evidence**: 23  
- **NA treated as Not Compliant due to lack of evidence or ownership**

These controls were grouped into categories to improve structure and accountability.
""")

# Recommendations
st.markdown("""
### ✅ Recommendations
> Network Security controls indicate wide gaps in visibility and ownership:
> - Define control ownership between networking, infrastructure, and security teams.  
> - Formalize implementation of built-in protections (e.g., ACLs, encryption, segmentation) with audit-ready evidence.  
> - Ensure proper DNS, routing, messaging, and wireless controls are validated and monitored.  
> - Assign responsibility for segmentation, endpoint protection, and secure routing.
""")

# Categorized summary (sampled)
data = {
    "Category": [
        "Network Perimeter & Filtering",
        "Traffic Control & Segmentation",
        "Network Management & Access Policies",
        "DNS & Name Resolution",
        "Wireless & Remote Access Security",
        "Secure Communication & Encryption"
    ],
    "Risk Rating": ["High"] * 6,
    "Status": [
        "Not Compliant",  # Most perimeter and filtering controls lack evidence
        "Not Compliant",  # Segmentation & ACLs marked NA or unclear
        "Not Compliant",  # Management controls have no evidence
        "Not Compliant",  # DNS and resolver integrity is not confirmed
        "Partially Compliant",  # Some controls are in place for remote and VPN access
        "Partially Compliant"  # Encryption via VPN and proxy confirmed, but not across all systems
    ]
}

# Display categorized table
st.subheader("📋 Categorized Network Security Summary")
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True, height=300)

# Export option
st.subheader("📤 Export View")
st.caption("Use browser print/PDF. PNG export available via html2image.")
