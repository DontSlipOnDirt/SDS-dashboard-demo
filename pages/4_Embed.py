import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Embed", page_icon="🖼️")

# embed spotify in a streamlit app
st.title("Embed")
st.write("Example of embed using `iframe` rendering with a Spotify playlist.")
components.iframe("https://open.spotify.com/embed/playlist/7nq356WLLUaT89Hn4q7e2z?utm_source=generator&theme=0", height=400)