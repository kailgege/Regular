'''
Created on 2019年11月18日

@author: 13476
'''
import re
from docx import Document

f=Document('test/AA.docx')
#string=input("需要查找的字符串：")

re_f=re.compile(u"[\u4e00-\u9fa5]+。") 
#re_f=re.compile(r'(.+|\s?)(Python.+[\u4E00-\u9FA5]+。)') 
re_f1=re.compile(u"Python.+[\u4E00-\u9FA5]+。")
re_f2=re.compile(r'\W(Python.+[\u4E00-\u9FA5]+。)') 
for fparagraph in f.paragraphs:
    findall_f=re_f1.findall(fparagraph.text)
    findall_f1=re_f1.findall(fparagraph.text)
    findall_f2=re_f2.findall(fparagraph.text)
    print(findall_f)
    #print(findall_f1)
    #print(findall_f2)