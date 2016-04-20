import pandas as pd

df = pd.read_csv('K:\\data\\JAPAN\\FOF\\Quarterly\\SAF\\34.csv')

##for index, row in df.iterrows():
##    print ( row[5])

print(df.columns.tolist()[:5])
print((typrdf))
for index, row in df.iterrows():
    print ( type(row))
