import pandas as pd
data ={
    "calories":[420,80,390],
    "duration": [50,45,40]    
}
df= pd.DataFrame(data,index=["day1","day2", "day3"])
print(df.loc["day2"])











































