import pandas as pd


s = pd.Series([1,2,3,4,5], index=['a', 'b', 'z', 'd', 'e'])
t = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
y=6
for i in s==t:
    y=y*i

print(y)
