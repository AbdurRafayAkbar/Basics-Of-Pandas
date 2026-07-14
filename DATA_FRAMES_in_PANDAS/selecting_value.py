import pandas as pd

data={
    "name":["Rafay","Hadi","Afaq"],
    "age":[22,20,25]
}

df=pd.DataFrame(data)
#selecting value using loc 
print(df.loc[0])