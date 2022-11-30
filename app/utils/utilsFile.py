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
        st.success("Got Your File, You can switch to Analyze Page")
        with open("dataset.csv", "wb") as f:
            f.write(file.getbuffer())


class Anadata:

    def __init__(self):
        try:
            self.df = pd.read_csv('dataset.csv', index_col=None)
            st.title("Analyze Phase")
            self.first_row()
            self.second_row()
        except pd.errors.EmptyDataError as e:
            st.error("No Data to write (Uploaded Data File is Empty)")

    def first_row(self):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Describer")
            st.dataframe(pd.DataFrame(self.df.describe(include='all')))

        with col2:
            st.header("Correlation Matrix")
            st.dataframe(pd.DataFrame(self.df.corr()))

    def second_row(self):
        st.header("Correlation Matrix Chart")
        corr_matrix = self.df.corr()
        st.plotly_chart(px.imshow(corr_matrix, text_auto=True, aspect='auto'))

        choice_2 = st.radio("Do You want target to correlate ?", [
                            'Yes', 'No'], horizontal=True)

        if choice_2 == 'Yes':
            columns = list(self.df.columns)
            columns.pop(0)
            # columns.insert(0, "Select")
            target_column = st.selectbox(
                "What is your target columns ? ", columns)
            if target_column != None:
                try:
                    target_corr_matrix = self.df.corr().sort_values(
                        by=target_column, ascending=False)
                    st.plotly_chart(px.imshow(target_corr_matrix,
                                    text_auto=True, aspect='auto'))
                except KeyError as error:
                    st.error(f"{error} Can be treated as Target Value")
        else:
            pass
