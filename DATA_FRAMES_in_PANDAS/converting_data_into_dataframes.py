import pandas as pd

data={
    "name":["Rafay","Hadi","Afaq"],
    "age":[22,20,25]
}
print(f"before data frame => {data}")

df=pd.DataFrame(data)

print(f"after data frame => {df}")