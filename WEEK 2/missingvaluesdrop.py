import pandas as pd
import numpy as np
df = pd.DataFrame({'AGE': [25, 30,np.nan, 40 , 35],
                   'Department': ['HR',  'Finance',np.nan, 'Finance', 'IT']})
print("Original DataSet")
print(df)

df_drop_rows = df.dropna()
print("After Dropping Rows :\n",df_drop_rows)

df_drop_columns = df.dropna(axis=1)
print("After Dropping Columns :\n",df_drop_columns)