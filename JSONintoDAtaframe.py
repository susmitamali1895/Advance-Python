import pandas as pd
df = pd.read_json('users.json')
print(df.to_string())
