#13) Write a Pandas program to combine many given series to create a DataFrame.
import pandas as pd
sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])


print("Original Series:")
print(sr1)
print(sr2)
print("Combine above series to a dataframe:")
ser_df = pd.DataFrame(sr1, sr2).reset_index()
print(ser_df.head())
print("\nUsing pandas concat:")
ser_df = pd.concat([sr1, sr2], axis = 1)
print(ser_df.head())
print("\nUsing pandas DataFrame with a dictionary, gives a specific name to the columns:")
ser_df = pd.DataFrame({"col1":sr1, "col2":sr2})
print(ser_df.head(5))
