import streamlit as st
from streamlit_local_storage import LocalStorage


localS = LocalStorage()

user = localS.getItem("User")
if user:
    st.write(f"User found in local storage: {user}")
else:
    st.write("No user found in local storage")





