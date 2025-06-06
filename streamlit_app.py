import streamlit as st
from PIL import Image
import pytesseract
import io

# Page config
st.set_page_config(page_title="Slide Analyzer", layout="wide")
st.title("🧠 Project Slide Analyzer")

# Load and display the image
image_path = "4605267d-da9b-4719-8fd9-2eeab4aca5f3.png"
image = Image.open(image_path)

st.subheader("📷 Uploaded Slide")
st.image(image, use_column_width=True)

# OCR extraction
st.subheader("🔍 Extracted Insights")
text = pytesseract.image_to_string(image)

with st.expander("Show Raw OCR Text"):
    st.text_area("Extracted Text", text, height=300)

# Simple logic to extract sections from OCR
st.subheader("📌 Summary")

if "Objective" in text:
    st.markdown("### 2.1 Objective")
    st.write("Evaluate the maturity of existing controls and identify control gaps across the Zerto datacenter environment.")

if "Executive Sponsor" in text:
    st.markdown("### 2.2 Executive Sponsor")
    st.write("Fidelma Russo")

if "Scope of Testing" in text:
    st.markdown("### 2.3 Scope of Testing")
    st.write("""
    - 227 controls assessed across 16 security domains  
    - All controls are critical (weight 9–10)  
    - Covered infrastructure includes VMware, IT systems, DevOps pipelines, and development tools  
    - Defined collaboratively between HPE and Zerto leadership  
    - Domains based on business impact, maturity, and risk relevance
    """)

st.markdown("---")
st.info("You can extend this app to include AI-based entity extraction or a comparison with prior slides for version tracking.")
