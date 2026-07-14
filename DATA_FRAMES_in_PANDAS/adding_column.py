import pandas as pd

data={
    "name":["Rafay","Hadi","Afaq"],
    "age":[22,20,25]
}

pd=pd.DataFrame(data)

pd["salary"]=[25552,155521,616311]

print(pd)