import pandas as pd
import numpy as np

path_to_folder_load= 'C:Users/jurge/Desktop/Python/'
file_name= 'Euro_2012_stats_TEAM.csv'

df_euro2012 = pd.read_csv(path_to_folder_load + file_name)

#2
#print(df_euro2012[["Goals"]])
print (df_euro2012.sort_values(by=['Goals', 'Passes'], ascending=[True, False]))
