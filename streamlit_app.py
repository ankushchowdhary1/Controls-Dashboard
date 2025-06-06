import streamlit as st
import pandas as pd

# Setup
st.set_page_config(layout="wide")
st.title("🧰 Maintenance Controls (10) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 10  
- **Compliant**: 1  
- **Not Compliant**: 1  
- **Not Assessed (NA)**: 8  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> Formalize maintenance control ownership and documentation.  
> - Assign accountable owner for each process.  
> - Document all remote activities, notifications, encryption safeguards.  
> - Enforce audit readiness for both internal and vendor-conducted maintenance.
""")

# Table Summary
data = {
    "Category": ["Maintenance"],
    "Total Controls": [10],
    "Compliant": [1],
    "Not Compliant": [1],
    "NA": [8]
}
df = pd.DataFrame(data)

# Display summary table
st.subheader("📋 Maintenance Control Summary")
st.dataframe(df, use_container_width=True, height=150)

# Export Option
st.subheader("📤 Export Summary")
st.caption("Use your browser's print or save-as-PDF feature. For PNG, use html2image integration.")
