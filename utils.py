import pandas as pd 

def clean_data(dataframe):
    # change BillNo, CustomerID to string
    dataframe['BillNo'] = dataframe['BillNo'].astype(str)
    dataframe['CustomerID'] = dataframe['CustomerID'].astype(str)
    
    #change Date to datetime
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='%d/%m/%Y %H:%M')
    
    # drop NaN values since it is all NaN for all columns in the test data
    dataframe.dropna(inplace=True)