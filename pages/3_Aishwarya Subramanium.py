import streamlit as st

st.set_page_config(
    page_icon="./ia-removebg-preview.png"
)

intdesc = "<p style='font-size:17px'></p>"
st.markdown(intdesc,unsafe_allow_html=True)

interview = "<h3 style = 'text-align:center'>Interview</h3>"
st.markdown(interview,unsafe_allow_html=True)
st.audio("./int3.mp3")
with open("./aishint.txt") as f:
    for line in f:
        st.write(line+"\n")