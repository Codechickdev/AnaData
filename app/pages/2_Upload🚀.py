import streamlit as st

from utilities.Upload import upload_dataset

with st.sidebar:
    choice = st.radio(
        'What you need to Upload', ["Dataset", "Model"]
    )

if choice == 'Dataset':
    st.title("Upload Your Dataset")
    st.info(
        "Note: This Webapp is still in expiremental. So upload files below 200MB"
    )
    fileType = st.selectbox(
        "What file Type is this ?",
        ['csv', 'sqlite', 'json']
    )
    file = st.file_uploader("Upload Here")
    upload_dataset(file, fileType)

elif choice == 'Model':
    pass
