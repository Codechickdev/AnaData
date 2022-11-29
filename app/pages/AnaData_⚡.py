import streamlit as st
from utils.utilsFile import Anadata

st.set_page_config(
    page_title='AnaData',
    page_icon='🦄',
    # layout='wide'
)

st.title("AnaData - Upload and Analyze 🚀")

if __name__ == "__main__":
    app = Anadata()
    app.run()