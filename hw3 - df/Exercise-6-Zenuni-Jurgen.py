import pandas as pd
import numpy as np

path_to_folder_load= 'C:Users/jurge/Desktop/Python/'
file_name= 'Euro_2012_stats_TEAM.csv'

df_euro2012 = pd.read_csv(path_to_folder_load + file_name)

#6
# | "or" instead of & becuase & would requireall 3 teams to be in 1 team column
print(df_euro2012[
    (df_euro2012['Team'] == 'England')
    |
    (df_euro2012['Team'] == 'Italy')
    |
    (df_euro2012['Team'] == 'Spain')][['Team', 'Shooting Accuracy']])

