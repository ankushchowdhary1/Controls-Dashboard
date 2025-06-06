import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("🌐 Web Security Controls Overview (4 Total)")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 4  
- **Compliant**: 4  
- **Not Compliant / No Response**: 0  
""")

# Recommendations
st.markdown("""
### ✅ Recommendations
> Web security controls are fully implemented:
> - Continue leveraging SDLC practices to manage unauthorized code and secure development.  
> - Periodically review OWASP and DMZ strategies to align with current threat trends.  
> - Document team responsibilities and ensure all secure frameworks remain up-to-date.
""")

# Controls Table
data = {
    "Control Description": [
        "Unauthorized code",
        "Use of demilitarized zones",
        "Web security standard (OWASP) incorporated into SDLC",
        "Web application framework"
    ],
    "Risk Rating": ["High"] * 4,
    "Status": ["Compliant"] * 4
}

# Table display
st.subheader("📋 Web Security Control Table")
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True, height=300)

# Export
st.subheader("📤 Export View")
st.caption("Use browser print/PDF. PNG export available via html2image.")
