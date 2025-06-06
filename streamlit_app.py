import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Control Implementation Chart", layout="wide")
st.title("📊 Control Implementation Rates by Domain")

# Data
data = {
    "Domain": [
        "Security Operations", "Web Security", "Change Management", "Asset Management",
        "Physical & Environmental Security", "Secure Engineering & Architecture",
        "Technology Development & Acquisition", "Cloud Security", "Configuration Management",
        "Vulnerability & Patch Management", "Identification & Authentication", "Compliance",
        "Endpoint Security", "Network Security", "Maintenance", "Continuous Monitoring"
    ],
    "Implementation %": [
        100, 100, 80, 70,
        65, 60, 58, 55, 55,
        55, 44, 33,
        27, 27, 23, 18
    ]
}
df = pd.DataFrame(data)

# Sort for better layout
df = df.sort_values(by="Implementation %", ascending=True)

# Bar chart
fig = px.bar(
    df,
    x="Implementation %",
    y="Domain",
    orientation="h",
    title="Control Implementation Rates by Domain",
    color="Implementation %",
    color_continuous_scale=px.colors.sequential.Blues,
    height=700
)

fig.update_layout(
    xaxis_title="Implementation %",
    yaxis_title="Domain",
    font=dict(size=14),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=100, r=40, t=60, b=40)
)

# Display
st.plotly_chart(fig, use_container_width=True)

# Export to PNG
st.subheader("📤 Export")
if st.button("Export as PNG"):
    fig.write_image("control_implementation_chart.png")
    with open("control_implementation_chart.png", "rb") as f:
        st.download_button(
            label="Download PNG",
            data=f,
            file_name="control_implementation_chart.png",
            mime="image/png"
        )
