#12) Write a Pandas program to add a prefix or suffix to all columns of a given DataFrame
import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,19,25,49]})
print("Original DataFrame")
print(df)
print("\nAdd prefix:")
print(df.add_prefix("OO_"))
print("\nAdd suffix:")
print(df.add_suffix("_OYO"))
