import pandas as pd
data=[50,61,65,77]

series=pd.Series(data)

print(series)
updated_data=series.loc[2] =100
print(updated_data)
iloc_data=series.iloc[2] = 500
print(iloc_data)