import streamlit as st
from PIL import Image
import pytesseract
import io

# Page config
st.set_page_config(page_title="Slide Analyzer", layout="wide")
st.title("🧠 Project Slide Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload a slide image (PNG, JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display the image
    image = Image.open(uploaded_file)
    st.subheader("📷 Uploaded Slide")
    st.image(image, use_column_width=True)

    # OCR extraction
    st.subheader("🔍 Extracted Insights")
    text = pytesseract.image_to_string(image)

    with st.expander("Show Raw OCR Text"):
        st.text_area("Extracted Text", text, height=300)

    # Parsed summary
    st.subheader("📌 Summary")
    if "Objective" in text:
        st.markdown("### 2.1 Objective")
        st.write("Evaluate the maturity of existing controls and identify control gaps across the Zerto datacenter environment.")

    if "Executive Sponsor" in text:
        st.markdown("### 2.2 Executive Sponsor")
        st.write("Fidelma Russo")

    if "Scope of Testing" in text:
        st.markdown("### 2.3 Scope of Testing")
        st.write(\"\"\"\n
        - 227 controls assessed across 16 security domains  
        - All controls are critical (weight 9–10)  
        - Covered infrastructure includes VMware, IT systems, DevOps pipelines, and development tools  
        - Defined collaboratively between HPE and Zerto leadership  
        - Domains based on business impact, maturity, and risk relevance\n
        \"\"\")

else:
    st.info("Please upload a slide image to analyze.")

