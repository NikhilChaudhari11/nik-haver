import win32com.client as win32
import os

word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False
#doc_path = os.path.join('c:', os.sep, 'Users', 'User', 'Documents', 'python', 'progs', 'misc', 'formatting for isn', 'sectarianism.doc')
doc = word.Documents.Open(r'J:\PROC\INTL\nordic\sweden\H09 Monthly Capital Markets MSCI.doc')
