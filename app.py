import streamlit as st
import streamlit.components.v1 as components

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Dentsu-logo_black.svg/2560px-Dentsu-logo_black.svg.png", width=100)
st.sidebar.header("Custom Report #2")

st.sidebar.subheader("Map visualization showcasing media formats before and after Budget TopUps along with competitive media formats across key Vietnam markets")

st.image("https://eyesooh.com/platform/design/img/head_logo_black.png",width=250)

st.subheader("Map Visualization")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://www.google.com/maps/d/embed?mid=1NwhpJlbC1K8hhPViQRWZAm9kjyi0SgM&ehbc=2E312F", width=1250, height=850, scrolling=False)



