import pandas as pd 

calories={
    "Day 1":1500,
    "Day 2":1126,
    "Day 3":1511
}

series_calorize=pd.Series(calories)
print(series_calorize)

#updating values

updated_calories=series_calorize.loc["Day 2"] =769
print(f"updated_calories is {updated_calories}")
print("After Changing Value")
print(series_calorize)