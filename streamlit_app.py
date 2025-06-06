import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("🏢 Physical & Environmental Security Controls (19 Total)")

# Summary Section
st.markdown("""
### 📊 Summary
- **Total Controls**: 19  
- **Compliant**: 8  
- **Not Compliant / No Response**: 11  
""")

# Recommendations Section
st.markdown("""
### ✅ Recommendations
> While foundational physical protections are in place, gaps exist in formal documentation and ownership:
> - Assign responsibility for environmental monitoring, alarm systems, and supporting infrastructure.  
> - Upload and maintain evidence for controls marked "No response".  
> - Ensure visitor management, surveillance, and access policy compliance is periodically reviewed and audited.
""")

# Detailed Control Table
data = {
    "Control Description": [
        "Physical and environmental protection",
        "Role-based physical access",
        "Physical access controls",
        "Controlled ingress and egress points",
        "Physical security of offices, rooms and facilities",
        "Working in secure areas",
        "Intrusion alarms/surveillance equipment",
        "Visitor control",
        "Supporting utilities",
        "Fire detection devices",
        "Temperature and humidity controls"
    ],
    "Risk Rating": ["High"] * 11,
    "Status": [
        "Not Compliant", "Compliant", "Compliant", "Compliant",
        "Not Compliant", "Compliant", "Not Compliant", "Compliant",
        "Not Compliant", "Compliant", "Compliant"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Table Display
st.subheader("📋 Physical & Environmental Security Control Table")
st.dataframe(df, use_container_width=True, height=500)

# Export Section
st.subheader("📤 Export View")
st.caption("Use browser print/save or html2image for PNG export.")
