import numpy as np
import pandas as pd 
import read_csv as read
import date 
import clean_data as clean
import analysis

file_path = 'Bitcoin Historical Data (1).csv'

all_data = read.read_csv(file_path)
data = date.date(all_data)
data = clean.cleanData(data)
print(analysis.analyze_indicators(data['High'], data['Low'], data['Price'], data['Vol.']))

