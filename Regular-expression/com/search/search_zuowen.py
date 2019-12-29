'''
Created on 2019年12月28日

@author: 13476
'''
import re
from docx import Document

f=Document('test/zuowen.docx')

re_f=re.compile(u'[\u4e00-\u9fa5|\uff0c|\uff1b]+十八[\u4e00-\u9fa5|\uff0c|\uff1b]+') 
#re_f=re.compile(u"") 
for fparagraph in f.paragraphs:
    #p=fparagraph.text.split(u'\u3002|\uff01|\uff1f|\u2026')
    p=fparagraph.text.split(r"。")
    print(p)
    for item in p:
        #加if判断减去空的结果
        findall_f=re_f.findall(item) 
        #print(findall_f)