from tkinter import *
import glob
import win32api
import sys

def show_entry_fields():
   #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    path1 = 'J:\\PROC\\INTL\\'+e1.get()+'\\'+e2.get()+'\\'+'*'+e3.get()+'*.doc'
    for filename in glob.iglob(path1, recursive=True):
	    #print(filename)
	    win32api.ShellExecute(0, 'open', filename, '', '', 1)
	    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

master = Tk()
master.title('Get Procedures')
Label(master, text="Database").grid(row=0)
Label(master, text="Country").grid(row=1)
Label(master, text="Group Number").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.insert(10,"Nordic")
e2.insert(10,"Norway")
e3.insert(10,"O49")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

#Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='GetProc', command=show_entry_fields).grid(row=4, column=1, sticky=W, pady=4)

mainloop( )

print(sys.argv[1])
