#make website look better add info about people in Home.

import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="./ia-removebg-preview.png",
)

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style",unsafe_allow_html=True)

st.sidebar.success("Select example interviews above")

header = "<h2 style = 'text-align:center; font-family:Georgia;color:black'>About Me</h2>"
st.markdown(header,unsafe_allow_html=True)


img,text = st.columns([0.3,1])

with img.container():
    st.image("njimage.jpg")
    


with text:
    description = "<p style = 'font-size:17px; font-family:Georgia;color:black'>Hi, I am Ananth Narayan. I am a high school senior, who is very passionate about computer science.<br>In my free time I love to code, play guitar, and play video games. In this project project to learn more about the Indian Americans in my community. I wanted to see how their journeys were different, and how they were the same. Most importantly, I wanted to gain connections to my own communinity. If you are interested in the project or want to participate in an interview, please contact me.<br><img src='maily.png'> </p>"
    st.markdown(description,unsafe_allow_html=True)

project = "<h2 style = 'text-align:center; font-family:Georgia;color:black'>About this Project</h2>"
st.markdown(project,unsafe_allow_html=True)
prodesc = "<p style = 'font-size:17px; font-family:Georgia;color:black'>This project is about sharing the stories and journeys of Indian American Immigrants. I have recorded interviews of Indian Americans in the Buffalo Area involving their journeys, challenges and succeses coming from India to America. After that , I used artificial intelligence to transcribe the interview and convert it into text, to easily share them. If you are interested in any of these interviews below please check them out.<br><br><a href='http://localhost:8501/Arup_Sen'>Arup Sen</a> - shows the importance of hardwork, regardless of oppurtunity value.<br><br><a href='http://localhost:8501/Sibu_Nair'>Sibu Nair</a> - reveals the importance of retaining Indian culture in America.<br><br><a href='http://localhost:8501/Aishwarya_Subramanium'>Aishwarya Subramanium</a> - reveals that coming to a new environment can be difficult but it can also help you thrive and learn more about yourself.</p>"
st.markdown(prodesc,unsafe_allow_html=True)

