'''
Created on 2019年12月13日

@author: 13476AA
'''
import re
from docx import Document

f=Document('test/English.docx')

re_f=re.compile(r'.*confidence.*',re.I) #re.I忽略大小写
re_p=re.compile(r'\.|\?|\!') 
for fparagraph in f.paragraphs:
    #p=fparagraph.text.split('.')
    p=re.split(re_p,fparagraph.text)
    for item in p:
        #加if判断减去空的结果
        findall_f=re_f.findall(item) 
        for find_f in findall_f:
            print(find_f+'.')