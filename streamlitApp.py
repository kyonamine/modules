import streamlit as st
import firstFile
import secondFile
import pandas as pd

def printout():
    f'{firstFile.func()} {secondFile.func()}'

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["pw"] == st.secrets["pw"]:
            st.session_state["password_correct"] = True
            del st.session_state["pw"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change = password_entered, key = "pw"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change = password_entered, key = "pw"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True
    
def uploadFile(descriptionStr):
    uploaded_file = st.file_uploader(descriptionStr, type = ['csv', 'txt'])
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file, dtype = {'Yext ID': str})
        dataframe = dataframe.dropna()
        dataframe = dataframe.astype(str)
        st.write(dataframe)
    return dataframe

def parseFile(df):
    listYextIds = df['Yext ID'].tolist()
    return listYextIds

printout()