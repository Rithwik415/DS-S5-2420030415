import pandas as pd

df = pd.DataFrame({'Name': ['ALICE', 'BOB', 'CHARLIE', 'DAVID']})
df['Name_lower'] = df['Name'].str.lower()
df['Name_upper'] = df['Name'].str.upper()

print(df)