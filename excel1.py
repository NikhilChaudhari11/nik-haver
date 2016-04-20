import xlwings as xw
import string
import itertools
from collections import OrderedDict
wb=xw.Workbook(r'Copy of Copy of final codes-nikhil.xlsx')
#xw.Range('main', 'A1:C3').value

list1 = xw.Range('main', 'S51:S399').value

alphanumlist = list(string.ascii_uppercase) + list(range(0,9))

#----creating dictionary-----------------
list22 = []
a = dict(itertools.zip_longest(alphanumlist,list22))
print(a)
print(type(a))
##od = OrderedDict(sorted(a.items(), key=lambda x:x[1], reverse=True))
##print(od)
