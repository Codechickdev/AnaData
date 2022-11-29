import plotly.express as px
import streamlit as st
import pandas as pd
import os

def clear_session():
    path = os.path.join('dataset.csv')
    with open(path, "w") as f:
        f.close()

def upload():
    st.header("Upload Phase")
    st.warning(
        "Note: This Webapp is still in expiremental. So upload files below 200MB")

    fileType = st.selectbox("What file Type is this ?",
                            ['csv', 'sqlite', 'json'])

    if fileType != 'csv':
        st.warning("Sorry, this feature is under Developement")

    file = st.file_uploader("Upload Here")

    if file:
        st.success("Got Your File")
        with open("dataset.csv", "wb") as f:
            f.write(file.getbuffer())
class Anadata:

    def __init__(self):
        try:
            self.df = pd.read_csv('dataset.csv', index_col=None)
            self.analyze()
        except pd.errors.EmptyDataError as e:
            pass

    def extractInformation(self):
        pass

    def analyze(self):
        st.header("DataFrame of Uploaded File")
        st.dataframe(self.df)
