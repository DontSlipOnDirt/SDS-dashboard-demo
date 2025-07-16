import streamlit as st

st.set_page_config(
    page_title="Intro",
    page_icon="👋",
)

st.write("# Welcome to the dashboard demo")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    This dashboard demonstrates the capabilities of Streamlit and its integrability with several other components.
    """
)