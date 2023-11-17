import os
import glob
import pandas as pd
from typing import List

"""
Function to read files from a folder data/input 
and return a list of dataframes

args: input_path (str): folder's path for files 

return: list of dataframes
"""
path = "data/input"

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    # list files from a folder
    files = glob.glob(os.path.join(path, '*.xlsx'))
    # list of dataframes
    df_list = []
    for file in files:
            df_list.append(pd.read_excel(file, engine='openpyxl'))
        
    return df_list


if __name__ == "__main__":
    df_list = extract_from_excel(path)
    print(df_list)