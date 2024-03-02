import csv
import pandas as pd
import babypandas as bpd
import numpy as np
import os

# simulates live data by applying sliding window to pre stored TCP numpy array


# TODO: figure out how to upload .csv files into this file

# Whose laptop is being used


def read_csv_files(folder_path):
    dfs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('test_filtered.csv'):
            file_path = os.path.join(folder_path, filename)
            # Read the CSV file into a DataFrame, ignoring lines starting with '#'
            df = pd.read_csv(file_path, comment='#')
            dfs.append(df)
        
    # Concatenate DataFrames
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df

df = read_csv_files('C:\\Users\\Drago\BCI-P300-Magician\\DataResults')    #Change your name based on who it is that is running it

filtered = df['Comments'] == ' changecard '

filtered_df = filtered[filtered == True]

temp_df = (pd.DataFrame({'New_Trigger': filtered})).astype(int)

df['Trigger'] = temp_df

print(df)

def temp():
    print('Hello World')


# TODO: use functions defined in model_define.py to train




# TODO: use functions defined in model_define.py to analyze accuracy
