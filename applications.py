import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


# entry point
def run():
    st.set_page_config(
        page_title="Home page",
        page_icon="👋",
    )

    st.write("# Bonjour Data Management 04, comment allez vous ???")


if __name__ == "__main__":
    run()
