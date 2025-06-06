import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("🏢 Physical & Environmental Security Controls (19 Total)")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 19  
- **Compliant**: 11  
- **Not Compliant / No Response**: 8  
""")

# Recommendations
st.markdown("""
### ✅ Recommendations
> While key physical security mechanisms are in place, there are several gaps in evidence, response, and environmental monitoring:
> - Assign ownership for environmental safety, alarms, and surveillance controls.  
> - Ensure all compliant controls are backed by updated documentation and access logs.  
> - Address "No response" areas with process clarification, monitoring, and physical audits.
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
        "Temperature and humidity controls",
        "Equipment siting and protection",
        "Transmission medium security"
    ],
    "Risk Rating": ["High"] * 13,
    "Status": [
        "Not Compliant", "Compliant", "Compliant", "Compliant", "Not Compliant",
        "Compliant", "Not Compliant", "Compliant", "Not Compliant", "Compliant",
        "Compliant", "Compliant", "Compliant"
    ]
}

# Add remaining 6 controls
additional_controls = [
    "Power equipment and cabling security",
    "Emergency shutoff",
    "Emergency lighting",
    "Fire suppression",
    "Delivery and loading area security",
    "Protection from environmental threats"
]
data["Control Description"].extend(additional_controls)
data["Risk Rating"].extend(["High"] * 6)
data["Status"].extend(["Compliant", "Compliant", "Compliant", "Compliant", "Compliant", "Compliant"])

# DataFrame and display
df = pd.DataFrame(data)

st.subheader("📋 Full Control Table")
st.dataframe(df, use_container_width=True, height=600)

# Export option
st.subheader("📤 Export View")
st.caption("Use your browser’s print/save to PDF, or integrate html2image for PNG export.")
