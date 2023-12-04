"""
Help to create hyperlinks for the web page.
"""

import streamlit as st


def display_link(url, text):
    """
    Display a hyperlink.
    """
    st.markdown(f"<a href='{url}' target='_self'>{text}</a>", unsafe_allow_html=True)


if __name__ == "__main__":
    display_link()
