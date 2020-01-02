'''
Created on 2019年12月28日

@author: 13476
'''
import re
from docx import Document

f=Document('test/zuowen.docx')

string=input("需要替换的字符串：")
'''
unicode 标点符号     u"[\u3000-\u303f\ufb00-\ufffd]+"  unicode 中文字符  u'[\u4e00-\u9fa5]+'
只匹配中文：re_f=re.compile(u'[\u4e00-\u9fa5|\u3000-\u303f|\ufb00-\ufffd]*十八岁[\u4e00-\u9fa5||\u3000-\u303f|\ufb00-\ufffd]*') 
'''
#可匹配中文中混有英文
re_f=re.compile(u'[\w\W\u4e00-\u9fa5|\u3000-\u303f|\ufb00-\ufffd]*'+string+'[\w\W\u4e00-\u9fa5||\u3000-\u303f|\ufb00-\ufffd]*') 
re_p=re.compile(r'。|？|！|……')
for fparagraph in f.paragraphs:
    p=re.split(re_p,fparagraph.text)
    #print(p)            #输出分割后的句子
    for item in p:
        findall_f=re_f.findall(item)  
        for find_f in findall_f:
            print(find_f+'。')