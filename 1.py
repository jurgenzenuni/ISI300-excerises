import pandas as pd

# Replace 'your_file.csv' with the actual file path of your CSV file
file_path = 'c:/Datasets/realtor-data.zip.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Remove rows where the "state" column is not "New York"
df = df[df['state'] == 'New York']

# To completely remove the "prev_sold_date" column
df = df.drop("prev_sold_date", axis=1)

df = df.dropna()
# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned DataFrame to a new CSV file if needed
df.to_csv('real_estateclean5.csv', index=False)


# If you want to keep the cleaned DataFrame in memory, you can use df for further processing.
