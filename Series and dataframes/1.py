### import libraries ###
import pandas as pd
import numpy as np

### set up variables ###

# folder where file with data is
path_to_folder_load = 'C:/Users/jurge/Downloads/'
# name of file where data is
file_name = 'games.xlsx'


### load data ###
# load data from file into dataframe
df_games = pd.read_excel(path_to_folder_load + file_name)

print("### Here is the data")
#print(df_games)

#print ( df_games.info() )

print("### Some columns")
#print( df_games[  ["year","team"]  ] )

#slicing rows
#print ( df_games[2:4] )

#filtering rows
#print ( df_games [df_games["team"]== "Packers"])

#select rows by condition, select and
print (df_games[
    (df_games["team"]== "Packers")
     &
    (df_games["year"]== 2012 )
     |
    ( df_games["team"] == "Lions" )
     ])  

###adding rows
path_to_folder = 'C:/Users/jurge/Downloads/'
file_name = 'games_addendum.xlsx'
df_games_addendum = pd.read_excel(path_to_folder + file_name)
#extending
df_games_all = pd.concat([df_games, df_games_addendum])
print( df_games_all)
##resetting index
df_games_all.reset_index(inplace=True, drop=True)
print (df_games_all)



##print("### now save the data")
##file_to_save = 'isi_300_20230227.csv'
##df_games.to_csv(path_to_folder_load + file_to_save
##                , index=False)
