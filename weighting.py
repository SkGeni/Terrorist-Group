import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

df = pd.read_csv('gtd_cleaned.csv', sep=',', index_col=0, engine='python',parse_dates=True, encoding=None, tupleize_cols=None, infer_datetime_format=False)
df = df.drop(columns = ['iyear','imonth','iday'])
weight = random.sample(range(1,181692),181691)
weight = sorted(np.divide(weight,181692))
print(weight)
df ['weight'] = weight
for col_name in df.columns:
    if (df[col_name].dtype == 'object'):
        df[col_name] = df[col_name].astype('category')
        df[col_name+'num'] = df[col_name].cat.codes

#181691
print(df)
