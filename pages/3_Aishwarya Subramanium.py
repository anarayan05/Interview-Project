import streamlit as st

st.set_page_config(
    page_icon="./ia-removebg-preview.png"
)

intdesc = "<p style='font-size:17px; font-family:Georgia;color:black'>This interview featuring <b>Mrs. Subramanium</b>. She immigrated to the US due to her work. This interview reveals that coming to a new environment can be difficult but it can also help you thrive and learn more about yoursef.</p>"
st.markdown(intdesc,unsafe_allow_html=True)

interview = "<h3 style = 'text-align:center; font-family:Georgia;color:black'>Interview</h3>"
st.markdown(interview,unsafe_allow_html=True)
st.audio("./int3.mp3")
with open("./aishint.txt") as f:
    for line in f:
        st.write(line+"\n")