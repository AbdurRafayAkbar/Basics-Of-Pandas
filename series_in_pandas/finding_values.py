import pandas as pd
data=[50,61,65,77]

series=pd.Series(data)
print(series)
beginnig_value=series.loc[0]
print(f"Beginnig value is : {beginnig_value}")

