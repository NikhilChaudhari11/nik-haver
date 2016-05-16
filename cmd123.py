import re
import time
import os

def cmd1(line):
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
