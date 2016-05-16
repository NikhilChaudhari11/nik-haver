from xlwings import Range, Sheet, Workbook
import string
import itertools
from collections import OrderedDict
import xlrd
import pandas as pd
wb=Workbook(r'c:\autocalendar.txt')
allrows=Range('autocalendar','A1',wkb = wb).vertical.value
for rownum, row in enumerate(allrows):
    print(row)
    print(rownum)


import openpyxl
wb1 = openpyxl.load_workbook(r'c:\autocalendar.txt')
