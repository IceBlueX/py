# from combine_customer_main import *
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.rand(6, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.rand(6, 2), columns=['a', 'd'])

df2['b'] = 0
df2['c'] = 0

df = df1.append(df2, ignore_index=True)

print(df1)
print(df2)

print(df)
