#make website look better add info about people in Home.

import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="./ia-removebg-preview.png"
)
st.sidebar.success("Select example interviews above")

header = "<h2 style = 'text-align:center'>About Me</h2>"
st.markdown(header,unsafe_allow_html=True)

margin = 0

img,text = st.columns(2)

with img:
    st.image("./njimage.jpg")

with text:
    description = f"<p style = 'font-size:17px';margin-left:{margin}>Hi, I am Ananth Narayan. I am a high school senior, who is very passionate about computer science.<br>In my free time I love to code, play guitar, and play video games. </p>"
    st.markdown(description,unsafe_allow_html=True)

project = "<h2 style = 'text-align:center'>About this Project</h2>"
st.markdown(project,unsafe_allow_html=True)
prodesc = "<p style = 'font-size:17px'>This project is about sharing the stories of Indian American Immigrants.</p>"
st.markdown(prodesc,unsafe_allow_html=True)

