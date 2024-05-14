import pandas as pd

def preprocess(df,region_df):

    df = df[df['Season'] == 'Summer']
    # merge df with region_df
    df=df.merge(region_df,on='NOC',how='left')
    #dropping duplicate
    df.drop_duplicates(inplace=True)
    # One Hot Encoding
    df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)

    return df