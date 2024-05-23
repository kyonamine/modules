import streamlit as st
import firstFile
import secondFile
# import snowflake.connector as sf
from snowflake.snowpark.context import get_active_session

def printout():
    f'{firstFile.func()} {secondFile.func()}'

def snowflake():
    conn = st.connection("snowflake")
    df = conn.query("select * from YEXT_DATALAKE.DB4_ALPHA.TAGS_LISTINGS where 1  and partner_id = 638 and location_id in (62365949)")
    for row in df.itertuples():
        st.write(f'{row}')
    return

printout()
snowflake()