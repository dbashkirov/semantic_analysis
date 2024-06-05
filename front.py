import streamlit as st
import requests


URL = "localhost"
PORT = "8000"

text = st.text_area("Text to analyze")

# localhost == 127.0.0.1

if st.button("Predict", type="primary"):

    res = requests.get(f"http://{URL}:{PORT}/predict",
                    json={"text": text})

    st.text(res.text)