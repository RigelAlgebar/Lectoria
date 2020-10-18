"""Main module for the streamlit app"""
import streamlit as st
import awesome_streamlit as ast


# Import the pages of the App.


# For every page in the app use the format:
# import src.pages.PAGE

import src.pages.home2
import src.pages.dashboard


# Not sure about the following line. We will maybe deprecate it later in favor
# AWS Incognito.
#ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home2,
    "Analytics Dashboard": src.pages.dashboard,
    #"About": src.pages.about,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    


if __name__ == "__main__":
    main()