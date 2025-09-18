import pandas as pd
df = pd.read_csv('datanew.csv')
print(df.corr())
# the correlation number varies from -1 to 1
#1 = Good relation
#0.9 = good relation
#-0.9 = would be a good relation as 0.9
#0.2 Not a good relation
