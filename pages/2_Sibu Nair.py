import streamlit as st

st.set_page_config(
    page_icon="./ia-removebg-preview.png"
)

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style",unsafe_allow_html=True)

intdesc = "<p style='font-size:17px; font-family:Georgia;color:black'>This interview features <b>Mr. Nair</b>, the Director of the Indian Associan in Buffalo. Mr. Nair Immigrated here from West Bengal, and loves to serve his community. This interview reveals the importance of retaining Indian culture in America. Please listen to this interview and read the transcription to learn more about Mr. Nair.</p>"
st.markdown(intdesc,unsafe_allow_html=True)

interview = "<h3 style = 'text-align:center; font-family:Georgia;color:black'>Interview</h3>"
st.markdown(interview,unsafe_allow_html=True)
st.audio("./int2.mp3")
with open("./sibunairint.txt") as f:
    for line in f:
        st.write(line+"\n")