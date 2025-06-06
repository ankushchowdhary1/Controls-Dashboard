import streamlit as st
import pandas as pd

# Streamlit setup
st.set_page_config(layout="wide")
st.title("🛡️ Endpoint Security (12 Controls) Overview")

# Summary
st.markdown("""
### 📊 Summary
- **Total Controls**: 12  
- **Compliant**: 5  
- **Not Compliant / No Response**: 6  
- **Clarification Needed**: 1 (SentinelOne capabilities unclear)  
""")

# Recommendation
st.markdown("""
### ✅ Recommendation
> Endpoint tooling is strong, but process and control attribution is weak.
> - Confirm SentinelOne coverage for anti-malware, EDR, firewall, etc.
> - Assign dedicated ownership for endpoint compliance validation.
> - Resolve all “no response” status items via workshops and internal testing.
""")

# Control Table
data = {
    "Control Description": [
        "Endpoint security controls implementation", "Endpoint protection measures for CIA",
        "Prohibit installation without privileged status", "Malicious code protection (anti-malware)",
        "Automatic antimalware signature", "Always-on protection", "Software firewall",
        "Endpoint detection and response (EDR)", "Host intrusion detection and prevention systems (HIDS/HIPS)",
        "Phishing and spam protection", "Trusted path", "Collaborative computing devices"
    ],
    "Status": [
        "Compliant", "Compliant", "No response", "No response", "No response", "No response",
        "No response", "No response", "No response", "Compliant", "Compliant", "Not compliant"
    ],
    "Risk Rating": ["High"] * 12
}
df = pd.DataFrame(data)

# Display table
st.subheader("📋 Control Compliance Table")
st.dataframe(df, use_container_width=True, height=700)

# Export note
st.subheader("📤 Export One-Pager")
st.caption("Use browser print/save or integrate with html2image for PNG/PDF automation.")
