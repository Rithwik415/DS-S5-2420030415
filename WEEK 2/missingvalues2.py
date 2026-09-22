import pandas as pd
import numpy as np
df = pd.DataFrame({'AGE': [25, 30,np.nan, 40 , 35],
                   'Department': ['HR',  'Finance', 'Finance' ,np.nan, 'IT']})
print("Original DataSet (with Missing values):")
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)

import pandas as pd
import numpy as np
df = pd.DataFrame({'AGE': [25, 30,np.nan, 40 , 35],
                   'Department': ['HR',  'Finance', 'Finance' ,np.nan, 'IT']})
print("Original DataSet (with Missing values):")
print(df)
df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)