import pandas as pd
import numpy as py

def date(data):
    new_data = {}
    user_date = input('date:')
    date = pd.to_datetime(data['Date'])
    ind = date[date == user_date].index
    print(ind.tolist())
    for i in data:
        new_data[i] = data[i].iloc[ind[0]-20:ind[0]]
    return new_data
