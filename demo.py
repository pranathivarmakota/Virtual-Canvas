import streamlit as st
import subprocess
import cv2
from aircanva import air_canva
st.markdown("<h1>Virtual Canvas</h1>",unsafe_allow_html=True)
st.markdown("<button>Get started!!</button>",unsafe_allow_html=True)
#st.markdown("<a href = 'http://localhost/canva/aircanva.py'></a><button>Get Started</button>",unsafe_allow_html=True)
@st.cache_data
def my_app():
    subprocess.Popen("streamlit run my_app.py")
    # your app code here
pass
if __name__ == "_main_":
    my_app()