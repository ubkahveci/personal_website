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

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#--- Load Assets---
lottie_animation1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_n9lzznbu.json")
lottie_animation2 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_r6ahcm9f.json")
img_python_programming = Image.open("images/image1.jpg")
img_data_analytics = Image.open("images/image2.jpg")


# ---Header Section---
with st.container():
    st.subheader("Hi, I am Ugur :wave:")
    st.title("A Machine Learning Engineer from Turkey")
    st.write("I am passionate about using Python and Machine Learning to be more efficient and effective!")
    st.write("[Learn More at my LinkedIn profile>](https://www.linkedin.com/in/u%C4%9Fur-berkay-kahveci-742a5590/?locale=en_US)")

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
            - I recently investigated how wind energy production forecasts affect electricity price for the case of Turkey and found out that they are in fact related to each other. [Link is needed>]
            """
                )
        st.header("What I do in my spare time")
        st.write("##")
        st.write(
            """
            - I am learning Flask Web Framework as well as HTML and CSS.
            - I do small-scale projects to improve myself on object recognition from camera/stock videos using OpenCV library in Python [GitHub link].
            - Using machine learning algorithms together with data analytics techniques, I analyze open source data I found on the internet. [Link is needed].
            """
                )

    with right_column:
        st_lottie(lottie_animation1, height=300, key="wind")
        st.write("")
        st.write("")
        st.write("---")
        st_lottie(lottie_animation2, height=300, key="data_analytics")

with st.container():
    st.write("---")
    st.header("My Skills and Certificates")
    st.write("##")
    image_column, text_column = st.columns((1,3)) #text_column is two times larger than the image column width-wise
    with image_column:
        st.write("\n")
        st.image(img_python_programming, use_column_width='auto')
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(img_data_analytics, use_column_width='auto')
    with text_column:
        st.subheader("These are the skills that I use daily")
        st.write(
                """
                * Python Programming [Cert.>]
                * Data Analytics [Cert.>]
                * Tensorflow
                * Google Spreadsheets and MS Office
                * MATLAB
                """
                )
        st.write("---")
        st.subheader("Additional skills")
        st.write(
                """
                * Project Management - Obtained from MindSet Institute (Certificate only available as hardcopy)
                * SQL
                * Flask
                * HTML and CSS
                * Tableau
                """
                )

with st.container():
    st.write("---")
    st.subheader("Get In Touch with Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ugurkahveci15@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message..." required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()