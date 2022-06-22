import streamlit as st
import pandas as pd
import requests

st.title("World Population App")
st.markdown('<iframe src="https://embed.lottiefiles.com/animation/72439"></iframe>', unsafe_allow_html=True)
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
col1, col2 = st.columns(2)




st.markdown(
    "<style> body{text-align:center;} .css-ffhzg2 {background-color: #2a2f35;} </style>", unsafe_allow_html=True)