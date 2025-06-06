import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("🧪 Technology Development & Acquisition (TDA) Controls Overview")

# Summary Section
st.markdown("""
### 📊 Summary
- **Total Controls**: 29  
- **Compliant**: 13  
- **Not Compliant / No Response**: 16  
""")

# Recommendations
st.markdown("""
### ✅ Recommendations
> TDA controls are partially implemented with notable gaps in secure development practices:
> - Assign ownership for early-stage security like SBOM, code analysis, and threat remediation.  
> - Incorporate secure-by-default practices throughout the development lifecycle.  
> - Improve evidence collection and role clarity for developer responsibilities.
""")

# Grouped summary of controls by category
categories = [
    "Product Security Lifecycle Governance",
    "Secure Development Practices",
    "Code Quality & Testing",
    "Component & Configuration Security",
    "Developer Operations & Environment"
]

data = {
    "Category": categories,
    "Risk Rating": ["High"] * 5,
    "Status": [
        "Not Compliant",  # SBOM, developer training, role ambiguity
        "Partially Compliant",  # SDLC, maturity model in place but gaps in enforcement
        "Not Compliant",  # Lacking static/dynamic analysis and testing evidence
        "Compliant",  # Secure configuration and access restrictions present
        "Partially Compliant"  # Some processes followed but lacking coverage and documentation
    ]
}

df = pd.DataFrame(data)

# Table
st.subheader("📋 Categorized Control Summary")
st.dataframe(df, use_container_width=True, height=350)

# Export
st.subheader("📤 Export View")
st.caption("Use browser print/PDF. PNG export available via html2image integration.")
