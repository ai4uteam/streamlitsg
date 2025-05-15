import streamlit as st

st.title("My First Streamlit app")
st.write(
    "Hello Streamlit world")
name = st.text_input("Enter your name")
if name:
    st.write(f"hello, {name}")

button = st.button("Click me")

if button:
    st.write("I was clicked!")
else:
    st.write("waiting to be clicked")
st.checkbox("Check me")