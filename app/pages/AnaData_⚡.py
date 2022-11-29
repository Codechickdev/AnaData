import streamlit as st
from utils.utilsFile import Anadata, upload, clear_session

st.set_page_config(
    page_title='AnaData',
    page_icon='🦄',
    layout='wide'
)

st.title("AnaData - Upload and Analyze 🚀")

with st.sidebar:
    choice = st.button('Clear Session')

if __name__ == "__main__":
    upload()
    if not choice:
        app = Anadata()
        app.run()
    if choice:
        clear_session()
