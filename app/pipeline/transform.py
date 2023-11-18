import pandas as pd
from typing import List

"""
function to transform a list of dataframes in an unique one
"""

def concat_data_frames(data_frames_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frames_list)