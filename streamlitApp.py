import streamlit as st
import firstFile
import secondFile
import snowflake.connector as sf
# from snowflake.snowpark.context import get_active_session

def printout():
    f'{firstFile.func()} {secondFile.func()}'

def snowflake():
    # f'{st.secrets.connections.snowflake}'
    # conn = st.connection("snowflake")
    conn = sf.connect(
        user = st.secrets["user"],
        password = st.secrets["password"],
        authenticator = 'https://yext.okta.com/',
        account = st.secrets["account"],
        role = st.secrets["role"] 
    )
    # st.write(conn)
    return conn

def snowflake2():
    sfConnection = snowflake()
    sfq = sfConnection.cursor()
    query = "select * from YEXT_DATALAKE.DB4_ALPHA.TAGS_LISTINGS where 1  and partner_id = 638 and location_id in (62365949)"

    sfq.execute(query)
    sfResult = sfq.fetchall()
    # for row in df.itertuples():
    st.write(f'{sfResult}')
    return

printout()
snowflake2()