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
#logging.basicConfig(level=logging.DEBUG)
g = Grab()

#--------------This is what you edit------------------------------------------
#***************************************************
#******************************************
#*******************************
whatsearch = 'saudi arabia data portal bulk download'
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
#print(str(count1))
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
            
        ##print(string.split())
        ##print(ks)
        common = set(ks).intersection(set(string.split()))
        print(list(common))
        rank = len(list(common))
        ##print(rank) # HOW MANY COMMON WORDS

        
            
        
##        if(all(i < rank for i in rankno)):
##            urllist=value
            

        ##print(rankno)
        rankno.append(len(list(common)))    
        
        ##print(value)
        ##print('-----------------------------')
#-------------end of for loop   end of function-----------------------------------------------------

    
    ##print(rankno, "  the length is   ", len(rankno))
    ##print(max(rankno))
    ##print(rankno.index(max(rankno)), 'best index')
    bestindex = rankno.index(max(rankno))
    bu = list(od.values())
    #for u in bu:
        ##print(u)
    ##print(len(bu))
    return(bu[bestindex])

    
besturl = rank(whatsearch)
##print('---------------------------------------')
print('This is the best URL found')
print(besturl)



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\end of url generation function\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



#-----------------setting path of download folder-----
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "D:\\nikhil\\python"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:\\Users\\Research18\\Documents\\py projects\\chromedriver.exe"
instan = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
#--------------------------------------------------------


#instan = webdriver.Chrome('C:\\Users\\Research18\\Documents\\py projects\\chromedriver.exe')
#instan = webdriver.Firefox()
instan.set_window_size(1200, 1000)
instan.execute_script("document.body.style.zoom='60%'")
#instan.get('http://87.101.205.104:6855/en/BulkDownload')
instan.get(besturl)
time.sleep(10)
#----------

#instan.execute_script("document.body.style.zoom='60%'")

#----------------------------------------------------------
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

time.sleep(2)
#-----------page 2 ---------------------------------------------
ids2 = instan.find_elements_by_xpath('//*[@id]')
lis2 = []
for ii in ids2:

        
        t = ii.get_attribute('id')#this is a string
        tex = instan.find_element_by_id(t).text
        if( tex.lower() == ('Population out of the Labour Force').lower()):
            lis2.append(t)
            
            #print('yay1')
        if( tex.lower() == ('Labor Force').lower()):
            #instan.find_element_by_id(t).click()
            #time.sleep(3)
            lis2.append(t)
            #print('yay2')
        if( tex.lower() == ('Employed Persons').lower()):
            #instan.find_element_by_id(t).click()
            #time.sleep(3)
            lis2.append(t)
            #print('yay3')
        if( tex.lower() == ('Unemployed Persons (15 Years And Over )').lower()):
            #instan.find_element_by_id(t).click()
            #time.sleep(3)
            lis2.append(t)
            #print('yay4')
        


#[instan.find_element_by_id(l).click() for l in lis2]
instan.find_element_by_xpath("//*[contains(text(), 'Select all')]").click()
time.sleep(2)
instan.implicitly_wait(2)
#------------------------
ids3 = instan.find_elements_by_xpath('//*[@id]')
lis3 = []
##for ii in ids3:
##        t = ii.get_attribute('id')#this is a string
##        tex = instan.find_element_by_id(t).text
##        print(t,'                      ',tex)


#--------hover-----and expand all-------------------------

element = instan.find_element_by_id('22600225')
#plus = instan.find_element_by_xpath("//*[@id='22600225']/td[1]/span[1]/span[1]")
hover = ActionChains(instan).move_to_element(element)
hover.perform()
time.sleep(1)

ActionChains(instan).context_click(element).perform()
instan.find_element_by_xpath("//*[contains(text(), 'Expand all')]").click()
#------------------------------------------------
#instan.execute_script("document.body.style.zoom='30%'")
lis5 = ['22595525', '16816025']
for i in range(16816625, 16817826,100):
    i = str(i)
    lis5.append(i)

[instan.find_element_by_id(l).click() for l in lis5]
##instan.find_element_by_xpath("//*[@id='22595525']/td[1]/span[1]/span[1]").click()
##instan.find_element_by_xpath('//*[@id="16800925"]/td[1]/span[1]/span[1]').click()
##instan.implicitly_wait(10)
time.sleep(1)
instan.find_element_by_id("DimInfoItem_14479025_907225").click()
time.sleep(1)
instan.find_element_by_xpath('//*[@id="FromCalendarCombo"]/div[1]').click()
instan.find_element_by_xpath('//*[@id="YEARS:1990"]').click()

instan.find_element_by_xpath('//*[@id="ToCalendarCombo"]/div[1]').click()
instan.find_element_by_xpath('//*[@id="YEARS:2016"]').click()

instan.find_element_by_xpath('//*[@id="DimInfoItem_14479025_14479225"]/div[3]').click()
instan.find_element_by_xpath('//*[@id="16783025"]').click()
instan.find_element_by_xpath('//*[@id="16783125"]').click()
instan.find_element_by_xpath('//*[@id="16783925"]').click()
instan.find_element_by_xpath('//*[@id="16784925"]').click() #main economic activity groups click
#--------hover-----and expand all-------------------------

#element1 = instan.find_element_by_id('16783125')

#element1 = instan.find_element_by_xpath('//*[@id="TreeList6318"]/div[2]/table')
#-----main econ explore------
gid = ["TreeList6317","TreeList6318","TreeList6319"]
ii=0
from selenium.common.exceptions import NoSuchElementException

element1 = None
while not element1:
    global ii
    try:
        element1 = instan.find_element_by_id(gid[ii])
    except NoSuchElementException:
        time.sleep(0.75)
        ii=ii+1

print(gid[ii])
time.sleep(0.5)
hover1 = ActionChains(instan).move_to_element(element1)
hover1.perform()
    
##try:
##    element1 = instan.find_element_by_id("TreeList6317")
##    time.sleep(0.5)
##    hover1 = ActionChains(instan).move_to_element(element1)
##    hover1.perform()
##except:
##    element1 = instan.find_element_by_id("TreeList6318")
##    time.sleep(0.5)
##    hover1 = ActionChains(instan).move_to_element(element1)
##    hover1.perform()
##    pass
##try:
##    element1 = instan.find_element_by_id("TreeList6319")
##    time.sleep(0.5)
##    hover1 = ActionChains(instan).move_to_element(element1)
##    hover1.perform()
##except:
##    element1 = instan.find_element_by_id("TreeList6316")
##    time.sleep(0.5)
##    hover1 = ActionChains(instan).move_to_element(element1)
##    hover1.perform()
##    
#-------------------


ActionChains(instan).context_click(element1).perform()
instan.find_element_by_xpath("//*[contains(text(), 'Expand all')]").click()
#------------------------------------------------
time.sleep(0.5)
#------------------ id generating function-----------------------------------    
def genn(start,end,inte):
    lis = []
    for i in range(start,end+inte,inte):
        i = str(i)
        lis.append(i)
    return(lis)
#----------------------------------------------------------------------------

aa = genn(16783225,16783725,100) #+ genn(16822525, 16822925, 100) + genn(23353225,23353725, 100)

aa.append('16827725')
aa.append('23353225')
aa= aa + genn(16822525,16822725,100) + genn(23353525,23353725,100)
aa.append('16822825')


#-----------------------------------------------------------
for l in aa:
    instan.find_element_by_id(l).click()
def scroll():
    for e in range(1,7):
        try:
            instan.find_element_by_xpath('//*[@id="ScrollBar6367"]/div[3]').click()
        except NoSuchElementException:
            time.sleep(0.5)
            instan.find_element_by_xpath('//*[@id="ScrollBar6368"]/div[3]').click()
time.sleep(1)        
scroll()
time.sleep(2)
instan.find_element_by_id('23353425').click() #agriculture,animalhusbandry&fishing
instan.find_element_by_id('16822925').click()
ab = ['23345025','16827825','16827925','16785325','16828025','16828125']
for l in ab:
    instan.find_element_by_id(l).click()
scroll()
ab = ['16785525','16786225']
ab = ab + genn(16828225, 16829025,100) + genn(16829125, 16829525,100)
time.sleep(1)
for l in ab:
    instan.find_element_by_id(l).click()
    #time.sleep(0.1)
#press next

#-----select sex------------------
instan.find_element_by_id("DimInfoItem_14479025_14479325").click()
time.sleep(1)

ab = ['16786925','16787025','16787125']
for l in ab:
    instan.find_element_by_id(l).click()

#--------------------------------------

#-----nationality------------------
instan.find_element_by_id("DimInfoItem_14479025_14479425").click()
time.sleep(1)

ab = ['16787225','16787325']
for l in ab:
    instan.find_element_by_id(l).click()

#--------------------------------------
for t in range(1,120):    
    instan.find_element_by_xpath('//*[@id="ScrollBar1793"]/div[3]').click() #scrolls the leftmost column

#-----round------------------
instan.find_element_by_id("DimInfoItem_14479025_14479525").click()
time.sleep(1)
instan.find_element_by_id('16787625').click() #half 1
#instan.find_element_by_id('16787725').click() #half 2
#--------------------------------------
instan.find_element_by_id("DimInfoItem_14479025_4312725").click()
time.sleep(1)

#--------hover-----and expand all-------------------------
element1 = instan.find_element_by_xpath('//*[@id="1"]')
time.sleep(0.5)
hover1 = ActionChains(instan).move_to_element(element1)
hover1.perform()
time.sleep(1)
ActionChains(instan).context_click(element1).perform()
instan.find_element_by_xpath("//*[contains(text(), 'Expand all')]").click()
#------------------------------------------------
ab = ['1']
ab = ab + genn(13579425,13579825,100)
for l in ab:
    instan.find_element_by_id(l).click()
#scroll
for e in range(1,9):
        instan.find_element_by_xpath('//*[@id="ScrollBar7619"]/div[3]').click()
        time.sleep(0.1)
        #instan.find_element_by_id("ScrollBar7620").click()
        
ab = ['101','13048925','13579325','106','105','104','103','102','16914125']
for l in ab:
    instan.find_element_by_id(l).click()
instan.find_element_by_id("ToolBarButton1658").click()
#------------
#----next page------
instan.find_element_by_id("ListItem8427").click()
instan.find_element_by_id("Button8511").click()


#instan.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
time.sleep(1)
instan.find_element_by_id("RadioButton9011").click()
time.sleep(1)
instan.find_element_by_id("Button9381").click()
time.sleep(15)
instan.quit()

#----------------------------------------------------
time.sleep(3)
ls_dir = os.listdir('D:\\nikhil\\python')    
for file in ls_dir:
    t = 'D:\\nikhil\\python\\'+file
    with zipfile.ZipFile(t, "r") as z:
      z.extractall("D:\\nikhil\\python")
time.sleep(2)
print('Deleting the .zip file')
for file in glob.glob(r'D:\\nikhil\\python\\*.zip'):
    os.remove(file)
time.sleep(1)
print('Current name of csv file is:\n%s' % os.listdir('D:\\nikhil\\python')[0])
print('Renaming the csv file as saudilabor.csv')
ls_dir1 = os.listdir('D:\\nikhil\\python')
for file in ls_dir1:
    t = 'D:\\nikhil\\python\\'+file
    os.rename(t,'D:\\nikhil\\python\\saudilabor.csv')
#----------------------Voila---------------------
print('Finished saving as .csv')
#------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\CMD time!!!//////////////////////////////
print('DEMONSTRATION:\n Typing...\n   QAMON\n   F:\qa\INTQA.xls')
time.sleep(5)
import re
line = """
#-------------------- write your cmd code here-------------------------------
QAMON
START /MAX F:\qa\INTQA.xls

 



















#-----------------------------------------------------------------------
"""
line = re.split("\n+", line)


def batch1(line):
    list11 = []
    for i in line:
        #print(i)
        if(type(i) != 'None' and len(i) != 0):
            #print(i.split()[0][0])
            e = i.split()[0][0]
            if( e != '#'):
              i=i.lstrip().rstrip()
              list11.append(i)
    
    return(list11)

    
list2 = batch1(line)
for i in list2:
    time.sleep(0.15)
    os.popen(i)
    time.sleep(0.15)

print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nWhatever you could do with CMD, you can do with this program :D !\n////////////////////////////////') 

