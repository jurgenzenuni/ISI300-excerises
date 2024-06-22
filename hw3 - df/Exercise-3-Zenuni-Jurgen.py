import pandas as pd
import numpy as np

path_to_folder_load= 'C:Users/gamer/Desktop/Python/'
file_name= 'Euro_2012_stats_TEAM.csv'

df_euro2012 = pd.read_csv(path_to_folder_load + file_name)

#3
print(df_euro2012 [["Team","Yellow Cards","Red Cards"]])
