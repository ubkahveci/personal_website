from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#--- Load Assets---
lottie_animation1 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_n9lzznbu.json")
img_python_programming = Image.open("images/image1.jpg")
img_data_analytics = Image.open("images/image2.jpg")


# ---Header Section---
with st.container():
    st.subheader("Hi, I am Ugur :wave:")
    st.title("A Machine Learning Engineer from Turkey")
    st.write("I am passionate about using Python and Machine Learning to be more efficient and effective in my life!")
    st.write("[Learn More at my LinkedIn profile>](https://tr.linkedin.com/in/uğur-berkay-kahveci-742a5590)")

#---What I do---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do at work")
        st.write("##")
        st.write(
            """
            In my role as research assistant:
            - I am building machine learning algorithms that effectively forecast renewable energy productions (especially wind energy related productions).
            - Also I am using signal processing techniques (transformations, time-frequency analysis etc.) to enhance the models and improve the forecasts.
            - I recently investigated how wind energy production forecasts affect electrivity price for the case of Turkey and found out that they are in fact related to each other. [Link is needed>]
            """
        )
        st.header("What I do in my spare time")
        st.write("##")
        st.write(
            """
            - I am building machine learning algorithms that effectively forecast renewable energy productions (especially wind energy related productions).
            - Also I am using signal processing techniques (transformations, time-frequency analysis etc.) to enhance the models and improve the forecasts.
            - I recently investigated how wind energy production forecasts affect electrivity price for the case of Turkey and found out that they are in fact related to each other. [Link is needed]
            """
        )

    with right_column:
        st_lottie(lottie_animation1, height=300, key="wind")

with st.container():
    st.write("---")
    st.header("My Skills and Certificates")
    st.write("##")
    image_column, text_column = st.columns((1,3)) #text_column is two times larger than the image column width-wise
    with image_column:
        st.write("\n")
        st.image(img_python_programming, use_column_width='auto')
        st.write("\n")
        st.image(img_data_analytics, use_column_width='auto')
    with text_column:
        st.subheader("These are the skills that I use daily")
        st.write(
                """
                * Python Programming [Cert.>]
                * Data Analytics [Cert.>]
                * MatLAB
                * Tensorflow
                * Google Spreadsheets
                """
        )
        st.subheader("and these are skills that I obtained but do not use daily")
        st.write(
                """
                * Project Management - Obtained from MindSet Institute (Certificate only available as hardcopy)
                * SQL
                * Flask
                * HTML and CSS
                * Tableau
                """
        )