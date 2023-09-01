import streamlit as st

st.set_page_config(
    page_icon="./ia-removebg-preview.png"
)

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style",unsafe_allow_html=True)

intdesc = "<p style='font-size:17px; font-family:Georgia;color:black'>This interview features <b>Mr. Sen</b>, an Indian American that imigrated to the U.S in 1971. His responses and stories reveal that while there are plenty of amazing oppurtunities in the U.S, oppurtunity isn't everything, and honest hard work is still very important. Please listen to Mr. Sen's interview and read the transcription below to learn more about his incredible journey</p>"
st.markdown(intdesc,unsafe_allow_html=True)

interview = "<h3 style = 'text-align:center; font-family:Georgia;color:black'>Interview</h3>"
st.markdown(interview,unsafe_allow_html=True)
st.audio("./int1.mp3")
with open("./interview1.txt") as f:
    for line in f:
        st.write(line+"\n")