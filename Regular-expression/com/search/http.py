'''
Created on 2020年1月10日

@author: 13476
'''
#urls=re.findall(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",text)
#emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
#pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') 
#这里我们需要的就是re.S 让'.'匹配所有字符，包括换行符。修改正则表达式为reg = re.compile('.*g_img={url: "(http.*?jpg)"', re.S)
#var username = /^[\u4E00-\u9FA5A-Za-z]+$/; or /^([a-zA-Z0-9\u4e00-\u9fa5\·]{1,10})$/  or  var reg = /^[\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20}$/;//验证姓名正则 
import re
from docx import Document

f=Document('test/http.docx')

re_f=re.compile(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)")
re_g = re.compile('.*g_img={url: "(http.*?jpg)"', re.S)
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