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
from selenium.webdriver import ActionChains
import zipfile
import glob
import os
#-----------------------------------------------------------------------
# list of country code tuples
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
#print(country.keys())
#--------------------------------------------------------------------------------------------
#/////////////////////////////////////////////////////////////
logging.basicConfig(level=logging.DEBUG)
g = Grab()
#--------------This is what you edit------------------------------------------
#***************************************************
#******************************************
#*******************************
whatsearch = 'central bank kuwait statistics monthly'
#*******************************
#******************************************
#***************************************************
#------------------------------------------------------------------------------
whatsearch = whatsearch.lower()
ws = whatsearch.split()
str2 = '+'.join(ws)
str1 = 'https://www.google.com/search?q='
str3 = str1 + str2
t = g.go(str3)
soup = BeautifulSoup(t.body, "lxml")
links = []
linkname =[]
thisLink1 = {}
#          *find the country and its isocode from the string input*
countnames = list(country.keys())
count1 = set(ws).intersection(set(countnames))
##print(ws)
##print(countnames)
print(str(count1))
y1 = str(count1).split("{'")[1].split("'}")[0]
isocode = country[y1]
#            **************parse html****
for link in soup.find_all('a', href=True):
    if link['href'] == '' or link['href'].startswith('#'):
        continue
    #ls = link.string.lower()
    
    thisLink = {
    'url': link['href'],
    'title': link.string
    }
    link1= (thisLink['url'].strip())
    if (link1 not in links) and ('google' not in link1) and ('search' not in link1) and ('?' not in link1):# and ('java' not in link1):#  and ( isocode in link1):#and ('?' not in link1):
        links.append(link1)
        linkname.append(thisLink['title'])
        thisLink1[thisLink['title']] = link1
#                   ************************
#-----------string ranking function-------------------------------
rankno = []
dict1 = {}
od = OrderedDict(sorted(thisLink1.items(), key=lambda x:x[1], reverse=True))


def rank(string):
    
    for key, value in od.items():
        if key is None:
         rankno.append(0)   
         continue
        
        key = key.lower()
        ks1 = key.split()
        ks =[]
        for y in ks1:
            pp = y.replace(',','')
            ks.append(pp)   
            
        print(string.split())
        print(ks)
        common = set(ks).intersection(set(string.split()))
        print(list(common))
        rank = len(list(common))
        print(rank) # HOW MANY COMMON WORDS

        
            
        
##        if(all(i < rank for i in rankno)):
##            urllist=value
            

        print(rankno)
        rankno.append(len(list(common)))    
        
        print(value)
        print('-----------------------------')
#-------------end of for loop   end of function-----------------------------------------------------

    
    print(rankno, "  the length is   ", len(rankno))
    print(max(rankno))
    print(rankno.index(max(rankno)), 'best index')
    bestindex = rankno.index(max(rankno))
    bu = list(od.values())
    for u in bu:
        print(u)
    print(len(bu))
    return(bu[bestindex])

    
besturl = rank(whatsearch)
print('---------------------------------------')
print(besturl)



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\end of url generation function\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

