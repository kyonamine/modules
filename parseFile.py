def parseFile(df):
    listGoogleIds = df['Google ID'].tolist()
    listYextIds = df['Yext ID'].tolist()
    return listYextIds, listGoogleIds