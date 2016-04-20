import pandas as pd
from xlwings import Range, Sheet, Workbook, view
import xlwings as xw
import string
import itertools
from collections import OrderedDict
import math
import re



wb=Workbook(r'D:\nikhil\new\Book1.xlsx')

codes = Range('Sheet2', 'F6:J649').value
##[print(i) for i in codes[:5]]
##print('---------------------')
##print(type(codes))
for i in codes:
    for j in range(1,5):
        if(math.modf(i[j])[0]==0):
            i[j]=int(i[j])
        #i[j]=str(i[j])
        i[j]=re.sub('[.]',',',str(i[j]))

##[print(i) for i in codes[:5]]


dfold = pd.DataFrame(codes, columns=['Code','Jan','Feb','Mar','Apr'])
print(dfold.head())
print('---------------------------------------------------------------')
##df = pd.DataFrame({'A': [0, 4, 5, 6, 7, 7, 6,5]})
##mapping = dict(enumerate([2,5,6,8,12,16,26,32]))
##df['D'] = df['A'].map(mapping)
##print (df)
wb1=Workbook(r'N:\nikhil\rus\russia cpi.xlsm')
codesnew = Range('Sheet12', 'H5:L988').value
for i in codesnew[:5]:
    for j in range(1,5):
        if(type(i[j])==float):
            i[j]=int(i[j])
        i[j]=str(i[j])
            

[print(i) for i in codesnew[:5]]
print('---------------------------------------------------------------')
dnew = pd.DataFrame(codesnew, columns=['Labels','Jan','Feb','Mar','Apr'])
print(dnew.head())
print('---------------------------------------------------------------')

listpandasold=[]

##for index, row in dfold.iterrows():
##    listpandasold.append(row.iloc[1:])

def equal1(x,y):
    tt=6
    for i in x==y:
        tt=tt*i
    return(tt)

dnew['Ext-Code'] = ""
print(dnew.head())

globallist = []

#--------------main function-----------------------------

#for index, row in dnew.iloc[:25].iterrows():
for index, row in dnew.iterrows():
    row1 = row.iloc[1:5]
    
    for i,r in dfold.iterrows():
        r1=r.iloc[1:]
        if( equal1(row1,r1)):
            #print('found it!')
            print((r.iloc[0])[:-9])
            globallist.append((r.iloc[0])[:-9])
            dnew.set_value(index,'Ext-Code',(r.iloc[0])[:-9])
    
#print(dnew.iloc[:15])
print('Unique codes matched are  ', len(set(globallist)))
#print(type(dnew['Ext-Code'].iloc[:30]))
##aa = dnew['Ext-Code'].iloc[:30]
##writelist = []
##for i in aa.iteritems():
##    writelist.append(i[1])
##print((writelist))

#Range('Sheet3','D1', wkb=wb).options(transpose=True).value = writelist1
view(dnew)

#Range('Sheet3','D1', wkb=wb).options(expand='vertical').value = [1, 2, 3]
#Range('Sheet3','D1', wkb=wb).options(transpose=True).value = [1, 2, 3]

