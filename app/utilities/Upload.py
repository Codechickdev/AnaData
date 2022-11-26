import streamlit as st
import pandas as pd


def upload_dataset(file, fileType):
    if fileType == 'csv':
        if file:
            st.info("Got your file")
            df = pd.read_csv(file, index_col=None)
            st.dataframe(df)

    elif fileType == 'sqlite':
        st.warning("Sorry, This feature is under developement", icon='⚙️')

    elif fileType == 'json':
        st.warning("Sorry, This feature is under developement", icon='⚙️')
