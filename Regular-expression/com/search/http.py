'''
Created on 2020年1月10日

@author: 13476
'''

import re
from docx import Document

f=Document('test/http.docx')

re_f=re.compile(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)")
#re_g = re.compile('.*g_img={url: "(http.*?jpg)"', re.S)
re_g = re.compile(r'http.*?[jpg|mp4|mkv|mp3]', re.S)
re_p=re.compile(r'\!|。|？|！|……')
for fparagraph in f.paragraphs:
    p=re.split(re_p,fparagraph.text)
    #print(p)            #输出分割后的句子
    for item in p:
        findall_f=re_f.findall(item)  
        #findall_g=re_g.findall(item) 
        #for find_g in findall_g:
        for find_f in findall_f:
            print(find_f)
            #print(find_g)