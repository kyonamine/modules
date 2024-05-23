import streamlit as st
import firstFile
import secondFile

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
    
def multiOptionSelect(descriptionString, optionsList):
    tupleOptions = tuple(optionsList)
    return st.radio(descriptionString, tupleOptions)