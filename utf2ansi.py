import sys
import os
import shutil
filepath = 'ppia.csv'
resultpath = 'ppia1.csv'
import codecs
content = codecs.open( filepath, "r", encoding = "utf-8" )
content1 = content.read()
contentres = codecs.open( resultpath, "w",encoding = "cp1252", errors = 'ignore')
contentres.write(content1)



