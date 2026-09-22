import pandas as pd
import numpy as np
df = pd.DataFrame({'AGE': [25, 30,np.nan, 40 , 35],
                   'Department': ['HR',  'Finance', 'Finance' ,np.nan, 'IT']})
print(df)

df['AGE']=df['AGE'].fillna(df['AGE'].mean())

df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)