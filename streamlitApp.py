import firstFile
import secondFile
import snowflake.connector as sf

def printout():
    f'{firstFile.func()} {secondFile.func()}'



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
connectToSF()
