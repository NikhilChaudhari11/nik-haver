import re
line = """
#-------------------- write your code here-------------------------------

a 
string 


my name is nikhil 
this is a batch file command
     trimmed?








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

    
print(batch1(line))
    