'''
Created on 2019年11月14日

@author: 13476
'''
import re
import docx
from docx import Document

f=Document('test/AA.docx')
#re_f=re.compile(r'Python')
re_f=re.compile(r'\w*Guido\w*')
for paragraph in f.paragraphs:
    findall_f=re_f.findall(paragraph.text)
    print(findall_f)
    print(paragraph.text)



