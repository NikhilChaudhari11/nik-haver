from xlwings import Range, Sheet, Workbook
import string
import itertools
from collections import OrderedDict
wb=Workbook(r'D:\nikhil\dict123.xlsx')
   

##list1 = Range('Sheet1', 'C1:C75').value
##
##list1 = [str(int(i)) for i in list1]
##
##labels1=[]
##for i in list1:
##    a = 'C'+i+'FUGR'
##    b = 'C'+i+'FOL'
##    c = 'C'+i+'FUAR'
##    labels1.extend((a,b,c))
##
##for u in labels1:
##    print(u)
##

##Range('Sheet1','D1', wkb=wb).options(transpose=True).value = labels1
##row=[]
##for i in range(5,81):
##    a = 'ROW#'+str(i)
##    row.extend((a,a,a))
##Range('Sheet1','F1', wkb=wb).options(transpose=True).value = row


list2 = Range('Sheet1', 'K1:M1').value
row1=[]
for i in range(1,76):
    row1.extend((list2[0],list2[1],list2[2]))
Range('Sheet1','O1', wkb=wb).options(transpose=True).value = row1

