import pandas as pd
import numpy as np

path_to_folder_load= 'C:Users/gamer/Desktop/Python/'
file_name= 'Euro_2012_stats_TEAM.csv'

df_euro2012 = pd.read_csv(path_to_folder_load + file_name)

#7
result_df=df_euro2012[
    (df_euro2012["Goals"] > 6)
    &
    (df_euro2012["Passes"] >= 4000)]
print(result_df)

#8
#FOLDER and FILE 
path_to_folder = 'C:Users/gamer/Downloads/'
file_name_csv='2012euro_exercise8.csv'
result_df.to_csv(path_to_folder + file_name_csv, index=True)
