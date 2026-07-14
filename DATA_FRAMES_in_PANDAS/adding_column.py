import pandas as pd

data={
    "name":["Rafay","Hadi","Afaq"],
    "age":[22,20,25]
}

df=pd.DataFrame(data)

#Add a new column
df["salary"]=[25552,155521,616311]

# Add new row

new_row=pd.DataFrame([{
    "name":"Haji",
    "age":51,
    "salary":5111221,
}])
df=pd.concat([df,new_row],ignore_index=True)
print(df)
