##import easygui
##import tkinter
##from tkinter import Tk
##from contextlib import contextmanager
##import smtplib
##import email
import pyautogui
import time
import os
from xlwings import Range, Sheet, Workbook
import string
import itertools
from collections import OrderedDict
##w = easygui.msgbox("Kuwait Mar-2016 data Out!", title="Nikhil's Alerts Manager")
##print(w)
##aa = easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))
##print(aa)
##easygui.msgbox("japan data Out!", title="Nikhil's Alerts Manager")
##easygui.msgbox("russia Mar-2016 data Out!", title="Nikhil's Alerts Manager")
##easygui.msgbox("almonds hahaha Mar-2016 data Out!", title="Nikhil's Alerts Manager")
##

#easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
##textbox(msg='hahah', title='apple ', text='banana', codebox=0)
##textbox(msg='second', title='orange ', text='pine', codebox=0)

##def tk(timeout=5):
##    root = Tk() # default root
##    root.withdraw() # remove from the screen
##
##    # destroy all widgets in `timeout` seconds
##    func_id = root.after(int(1000*timeout), root.quit)
##    try:
##        yield root
##    finally: # cleanup
##        root.after_cancel(func_id) # cancel callback
##        root.destroy()
##
##
##with tk(timeout=1.5):
##    easygui.msgbox('message')

##from tkinter import *
##
##class quitButton(Button):
##    def __init__(self, parent):
##        Button.__init__(self, parent)
##        self['text'] = 'Good Bye'
##        # Command to close the window (the destory method)
##        self['command'] = parent.destroy
##        self.pack(side=BOTTOM)
##
##root = Tk()
##quitButton(root)
##mainloop()

##SERVER = '192.168.1.253'
##FROM = 'research33@haver.com'
##
##TO = ["research33@haver.com"] # must be a list
##
##SUBJECT = "Hello!"
##
##TEXT = "This message was sent with Python's smtplib."
##
### Prepare actual message
##
##message = """\
##From: %s
##To: %s
##Subject: %s
##
##%s
##""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
##
### Send the mail
##
##server = smtplib.SMTP(SERVER)
####server.sendmail(FROM, TO, message)
####server.quit()
#------------------------------------------------------------
#START /MAX F:\qa\INTQA.xls
import re
line = """
#----------- write your cmd code here-----------
QAMON
del C:\\Users\\Research18\\Desktop\\out.csv

 



















#-----------------------------------------
"""
line = re.split("\n+", line)


def batch1(line):
    list11 = []
    for i in line:
        i = i.strip()
        if(type(i) != 'None' and len(i) != 0):
            #print(i.split()[0][0])
            #print('****',i, type(i))
            e = i.split()[0][0]
            #print(e)
            if( e != '#'):
              i=i.lstrip().rstrip()
              list11.append(i)
    
    return(list11)

#print(line)    
list2 = batch1(line)
#print(list2)
for i in list2:
    time.sleep(0.15)
    a = os.popen(i)
    print(']]***//    ',a)
    time.sleep(0.15)
#-----------------------------------------------------------------------------
#pyautogui.screenshot(r'C:\Users\Research18\Desktop\abcdefg.png')
##button7location = pyautogui.locateOnScreen('C:\\Users\\Research18\\Desktop\\right.png')
##print(button7location)
##button7x, button7y = pyautogui.center(button7location)
##pyautogui.moveTo(button7x, button7y, duration=0.25)
##for i in range(1,3):
##  #pyautogui.click(button7x, button7y)
##  pyautogui.click(x=1146, y=126)  
##  time.sleep(0.5)


pyautogui.click(x=1146, y=126)
time.sleep(0.6)
pyautogui.click(x=1146, y=126)
time.sleep(0.3)

pyautogui.click(x=1068, y=129)
##buttonlocation1 = pyautogui.locateOnScreen('C:\\Users\\Research18\\Desktop\\europe.png')
##buttonx1, buttony1 = pyautogui.center(buttonlocation1)
##pyautogui.moveTo(buttonx1, buttony1, duration=0.25)
##pyautogui.click(buttonx1, buttony1)
time.sleep(1.5)

##buttonlocation2 = pyautogui.locateOnScreen('C:\\Users\\Research18\\Desktop\\snap.png')
##print(buttonlocation2)
##buttonx2, buttony2 = pyautogui.center(buttonlocation2)
##pyautogui.moveTo(buttonx2, buttony2, duration=0.35)
##pyautogui.click(buttonx2, buttony2)

pyautogui.click(x=1016, y=346)
time.sleep(0.5)

def click1(x,y):
    pyautogui.click(x, y)
    time.sleep(0.5)
click1(1043,540)
click1(499,165)
click1(897,507)
click1(846,344)
click1(1183,543)
click1(1159,76)
wb=Workbook('C:\\Users\\Research18\\Desktop\\out.csv')
columnvalues1 = Range('A1').vertical.value
colindex = len(columnvalues1)
print(colindex)  #get last row index eg. row#15
rowvalues1 = Range('A1').horizontal.value
rowindex = len(rowvalues1) #last column index eg. col#M
print(rowindex)
#map numbers to alphabets-------------
di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))
for c in sorted(di.keys()):
    print ("{0}:{1}  ".format(c, di[c]))
#-------------------------------------
# total range = A1: 

