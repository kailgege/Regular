'''
Created on 2020年2月10日

@author: 13476
'''
import re
from docx import Document

f=Document('test/zuowenName.docx')

re_f=re.compile(r"/^[\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20}$/")
re_p=re.compile(r'\!|。|？|！|……')
for fparagraph in f.paragraphs:
    p=re.split(re_p,fparagraph.text)
    #print(p)            #输出分割后的句子
    for item in p:
        findall_f=re_f.findall(item)  
        for find_f in findall_f:
            print(find_f)