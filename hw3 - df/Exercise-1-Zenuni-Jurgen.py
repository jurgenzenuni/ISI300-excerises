import pandas as pd
import numpy as np

path_to_folder_load= 'C:/Users/gamer/Desktop/Python/'
file_name= 'Euro_2012_stats_TEAM.csv'

df_euro2012 = pd.read_csv(path_to_folder_load + file_name)

print("The data")
print(df_euro2012)

