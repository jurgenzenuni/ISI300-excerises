import pandas as pd

df = pd.read_csv('c:/Datasets/Salary_Data.csv')

#Updates the sal column to less than or more than 100K based on each persons salary
df['Salary'] = df['Salary'].apply(lambda x: '>100K' if x > 100000 else '<=100K')

df.to_csv('salary100k_dataset.csv', index=False)
