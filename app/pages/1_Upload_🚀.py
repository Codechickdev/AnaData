import streamlit as st
from utils.utilsFile import Anadata, upload, clear_session

st.set_page_config(
    page_title='AnaData',
    page_icon='🦄',
)

with st.sidebar:
    choice = st.button('Clear Session')

if __name__ == "__main__":
    upload()
    if choice:
        clear_session()
