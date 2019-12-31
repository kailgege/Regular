'''
Created on 2019年12月28日

@author: 13476
'''
import re
from docx import Document

f=Document('test/zuowen.docx')

#u"[\u3000-\u303f\ufb00-\ufffd]+"  "unicode 标点符号"   :\uff1a   ,\uff0c   ;\uff1b 
#re_f=re.compile(u'[\u4e00-\u9fa5|\uff0c|\uff1b|\uff1a]*十八岁[\u4e00-\u9fa5|\uff0c|\uff1b|\uff1a]*') 

re_f=re.compile(u'[\u4e00-\u9fa5|\u3000-\u303f|\ufb00-\ufffd]*十八岁[\u4e00-\u9fa5||\u3000-\u303f|\ufb00-\ufffd]*') 
re_p=re.compile(r'。|？|！|……')
for fparagraph in f.paragraphs:
    #p=fparagraph.text.split(r"。")
    p=re.split(re_p,fparagraph.text)
    #print(p)
    for item in p:
        #加if判断减去空的结果
        findall_f=re_f.findall(item)  
        for find_f in findall_f:
            print(find_f+'。')