import pandas as pd


def read_csv(file_path): 
    df = pd.read_csv(file_path)


    data = df.iloc[1:, :]
    return data

