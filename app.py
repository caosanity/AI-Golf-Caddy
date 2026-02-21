import streamlit as st
from golf_caddy import answer_query

st.title("🏌️ AI Golf Caddy")

user_input = st.text_input("Hi, I am your golf caddy. How can I help you today?")

if st.button("Get Recommendation"):
    if user_input:
        result = answer_query(user_input)
        st.write(result)
    else:
        st.warning("Please enter your preferences.")