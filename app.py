import streamlit as st

# Title
st.title("Welcome to My First Streamlit App!")

# Input box
name = st.text_input("What's your name?")

# Button
if st.button("Greet Me"):
    st.success(f"Hello, {name}! 👋 Welcome to the app.")
