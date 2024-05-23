import streamlit as st
import firstFile
import secondFile
# import snowflake.connector as sf
from snowflake.snowpark.context import get_active_session

def printout():
    f'{firstFile.func()} {secondFile.func()}'

def snowflake():
    session = get_active_session()
    f'{session}'
    return session


def connectToSF():
# def connectToSF(SF_DB_USERNAME, SF_DB_PASSWORD):
    # try:
    #     sfConnection = sf.connect(
    #         account="exa52539.us-east-1",
    #         user = "APP_TECHNOLOGY_OPERATIONS",
    #         password=SF_DB_PASSWORD,
    #         role="TECHNOLOGY",
    #         # warehouse="PROD_WORKFLOW",
    #         warehouse="APP_QUERY",
    #         # database="PROD_PLATFORM_LOCAL")
    #         database="TEAM_TECHNOLOGY_OPERATIONS")
    # except:
    #     SF_DB_USERNAME = "wzuo@yext.com"
    #     SF_DB_PASSWORD = ""
    #     sfConnection = sf.connect(
    #         user=SF_DB_USERNAME,
    #         account="tw61901.us-east-1",
    #         authenticator='externalbrowser',
    #         role="TECHNOLOGY",
    #         warehouse="HUMAN_WH",
    #         database="PROD_PLATFORM_LOCAL")
    # print("Got sfConnection")
    # return sfConnection
    SF_DB_USERNAME = "kyonamine@yext.com"
    SF_DB_PASSWORD = ""
    sfConnection = sf.connect(
        user = SF_DB_USERNAME,
        account = "exa52539.us-east-1",
        authenticator = 'externalbrowser',
        role = "TECHNOLOGY",
        warehouse = "HUMAN_WH",
        database = "PROD_PLATFORM_LOCAL")
    f'{sfConnection}'
    return sfConnection

printout()
# connectToSF()


snowflake()