'''
Created on 2019年11月7日

@author: 13476
'''
import re 

#定义要匹配的字符串
telephone='010-1234567'
email='1234789876@qq.com'
Id='444444198809097879'


#compile()函数编译正则表达式
re_phone=re.compile(r'^(\d{3})-(\d{3,8})$')
re_email=re.compile(r'^(\w{4,20})@(163|126|qq)(.com|.edu)$')
re_Id=re.compile(r'^(\d{6})(\d{4})(\d{2})(\d{2})(\d{4})$')


#使用
match_phone=re.match(re_phone,telephone)
match_email=re.match(re_email,email)
match_Id=re.match(re_Id,Id)


#输出
print(match_phone.groups())
print(match_email.groups())
print(match_Id.groups())
