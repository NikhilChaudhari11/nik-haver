from xlwings import Range, Sheet, Workbook

wb=Workbook(r'D:\n123\pyp\prg.xlsx')
origcodes = Range('Sheet1', 'A1:A33').value

newcodes = []
meancodes = []
for i in origcodes:
    i = i.strip()
    newcodes.append(i[:-1])
    meancodes.append(i[:-1] + 'B')

f = open(r"D:\n123\pyp\prgproject.txt",'w')



for i, n, m in zip(origcodes, newcodes, meancodes):
    #f.write("series %s=@nan(%s(-1)+(%s(-1)*(%s/100)),100)" % (n,n,n,i))
    txt = """series %s=@nan(%s(-1)+(%s(-1)*(%s/100)),100)
series %s=@recode(%s=100,NA,%s)

'Rebase to 2014=100
series %s=@mean(%s, "2014:01 2014:12")
series %s=(%s/%s)*100
series %s=@round(%s*1000)/1000
'-------------------------
""" % (n,n,n,i,n,n,n,m,n,n,n,m,n,n)
    f.write(txt)
    

for n in newcodes:
    f.write(str(n)+' ')

f.close()


