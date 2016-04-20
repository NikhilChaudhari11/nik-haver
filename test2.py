from bs4 import BeautifulSoup
from os import path
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from collections import OrderedDict
from grab import Grab
import logging

instan = webdriver.Ie("C:\\Users\\Research18\\Documents\\py projects\\IEDriverServer.exe")

# list of country code tuples
#-----------------------------------------------------------------------------------------------------------------------------------
import xlrd

workbook = xlrd.open_workbook("N:\\nikhil\\EMERGE1.xls")
sheet1=workbook.sheet_by_index(0)

col1 = sheet1.col_values(0)
col3=sheet1.col_values(2)
col2=sheet1.col_values(1)
col4=sheet1.col_values(3)
ciso = col2 + col4
cname = col1 + col3
cname = [i.lower() for i in cname]
ciso = [i.lower() for i in ciso]
country = zip(cname,ciso)
##for i in country:
##    print(i)
country = OrderedDict(sorted(dict(country).items(), key=lambda x:x[1], reverse=True))
#-------------------------------------------------------------------------------------------------------------------------------------
instan.get('http://87.101.205.104:6855/en/BulkDownload')
time.sleep(7)
ids = instan.find_elements_by_xpath('//*[@id]')
lis = []
rankno1 = []
getid1 = []
nextid = 0
#-----------------------getid1 function----------------------
def getid11(firststring):
    global nextid
    for ii in ids:
        
        t = ii.get_attribute('id')#this is a string
        tex = instan.find_element_by_id(t).text
        if(len(tex.split("\n"))==1):
            #print(t,"|||||||",  tex)
            tex = tex.lower()
            firststring = firststring.lower()
            common = set((firststring).split()).intersection(set(tex.split()))
            lis.append(tex)
            getid1.append(t)
##            print(t, '                                 ',tex)
##            print(tex.split())
##            print(firststring.split())
##            print(list(common))
            rank = len(list(common))
##            print(rank, ' # HOW MANY COMMON WORDS' ) # HOW MANY COMMON WORDS
##            print(rankno1)
            rankno1.append(len(list(common)))    
##            print(tex)
##            print('-----------------------------')
            if( tex == 'next'):
                nextid = t

    bestindex = rankno1.index(max(rankno1))
    return(getid1[bestindex])
#-------------------------------------------------------------

bestid = getid11('Labor Force Indicators')

instan.find_element_by_id(bestid).click()
instan.find_element_by_id(nextid).click()

time.sleep(5)

print('the control is here')



