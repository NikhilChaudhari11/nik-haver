import zipfile
import os
import glob

ls_dir = os.listdir('D:\\nikhil\\python')


for file in ls_dir:
    print(file)
    t = 'D:\\nikhil\\python\\'+file
    with zipfile.ZipFile(t, "r") as z:
      z.extractall("D:\\nikhil\\python")



##for file in glob.glob(r'D:\\nikhil\\python\\*.txt'):
##    os.remove(file)                                                                                                                                        
##    
