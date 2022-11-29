import streamlit as st
import pandas as pd

class Anadata:

    def __init__(self):
        self.file = None

    def upload(self):
        with st.container():
            st.header("Upload Phase")
            st.warning(
                "Note: This Webapp is still in expiremental. So upload files below 200MB")

            fileType = st.selectbox("What file Type is this ?",
                                    ['csv', 'sqlite', 'json'])

            if fileType != 'csv':
                st.warning("Sorry, this feature is under Developement")

            file = st.file_uploader("Upload Here")

            if file:
                st.info("Got Your File")
                self.file = file
    
    def analyze(self):
        print(self.file.type)

    def run(self):
        self.upload()
        if self.file:
            self.analyze()
