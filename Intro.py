import streamlit as st

st.set_page_config(
    page_title="Intro",
    page_icon="👋",
)

st.write("# Welcome to the LLM dashboard")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    This dashboard demonstrates some of the capabilities of LLMs. In the sidebar you can find:
    - Chat
    - Figure generation
    - RAG discussion
"""
)
