import pandas as pd

'''The below data exploration discovered that the dataset has no missing or duplicated entries. All columns except for date contain numbers (either integers or floats). The number of unique values in each column make sense based on the context of the dataset. Overall the data appears clean.'''

line = "-----------------------------------"

house_df = pd.read_csv("Housing.csv")

print(house_df)
print(line)
cols = house_df.columns.tolist()
print("Column names: " , cols)
print(line)
print("Missing values: \n" , house_df.isna().sum())
print(line)
print("Duplicated entries: " , house_df.duplicated().sum())
print(line)
print("Unique values: \n" , house_df.nunique())
print(line)
print("Data types: \n" , house_df.dtypes)