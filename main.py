import numpy as np
import pandas as pd 
import read_csv as read
import date 
import clean_data as clean
import analysis
import functions as f
import label
import test2 as tst
import indicators as indc

file_path = 'XRP Historical Data.csv'

all_data = read.read_csv(file_path)
data = clean.cleanData(all_data)
all_data = label.label2(all_data)
all_data = indc.indicators(all_data)
print(tst.test(all_data))

