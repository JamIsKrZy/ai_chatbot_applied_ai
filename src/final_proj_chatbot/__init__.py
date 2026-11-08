import streamlit as st
from streamlit_local_storage import LocalStorage

st.set_page_config(page_title="Power Scaling ❤️‍🔥❤️‍🔥❤️‍🔥", layout="centered")

pages = [
    st.Page("pages/arena.py", title="Arena", icon="👋", default=True),
    st.Page("pages/create_character.py", title="Create Character", icon="👋"),
    # st.Page("about_me.py", title="About Me", icon="👋"),
    # st.Page("portfolio.py", title="Portfolio", icon="🗂️"),
    # st.Page("projects.py", title="Projects", icon="🛠️"),
]

navigation = st.navigation(pages, position="top")

localS = LocalStorage()

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def main() -> None:

    
    localS.setItem("User", User(name="James", age=20).__dict__)
    
    

    navigation.run()


if __name__ == "__main__":
    main()