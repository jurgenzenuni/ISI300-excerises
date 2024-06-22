import pandas as pd

df = pd.read_csv('c:/Datasets/Salary_Data.csv')

#remove duplicate degree levels
df['Education Level'] = df['Education Level'].replace("Bachelor's", "Bachelor's Degree")

df['Education Level'] = df['Education Level'].replace("Master's", "Master's Degree")

#Updates the sal column to less than or more than 100K based on each persons salary
# df['Salary'] = df['Salary'].apply(lambda x: '>100K' if x > 100000 else '<=100K')

df.to_csv('salaryREGR.csv', index=False)



#Updates the sal column to less than or more than 100K based on each persons salary
# df['Salary'] = df['Salary'].apply(lambda x: '>100K' if x > 100000 else '<=100K')
# df['Salary'] = df['Salary'].apply(lambda x: '<=50K' if x <= 50000 else ('<=100K' if x <= 100000 else '>100K'))