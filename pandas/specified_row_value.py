#11) Write a Pandas program to get the specified row value of a given DataFrame
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("Value of Row1")
print(df.iloc[0])
print("Value of Row4")
print(df.iloc[3])
