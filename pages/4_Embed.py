import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Embed", page_icon="🖼️")

# embed spotify in a streamlit app
st.title("Embed")
st.write("Examples of embed using `iframe` embedding.")
components.iframe("https://open.spotify.com/embed/playlist/7nq356WLLUaT89Hn4q7e2z?utm_source=generator&theme=0", height=400)
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vS3OXR9WlHmD-9i9IKhe_dAzGJ9i-bO4_vfPetV8FzF3ZPJXSG4JubbQhFrJlv-izrXh-48c0jbX3qM/pubembed?start=false&loop=false&delayms=3000", height=400)