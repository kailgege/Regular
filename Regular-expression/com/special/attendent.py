'''
Created on 2020年4月7日

@author: 13476
'''
import re
import xlrd 

Studentid=[]
Signid=[]

wb=xlrd.open_workbook(u'data/ZX2300398101-20200310_一班学生.xlsx')
sheet=wb.sheet_by_index(0)

rows=sheet.nrows
for i in range(6,rows):
    Studentid.append(sheet.cell_value(i,0).strip())
'''
lenStudentid=len(Studentid)
print(lenStudentid)
a=0   
for a in range(lenStudentid-1):
    print(Studentid[a])
    #print(type(Studentid[a]))
'''

with open('data/1.txt','r') as f:
   str=f.read() 

#re_str=re.compile(r'^([0-9]+)\n1{1}$',re.M)
re_str=re.compile(r'^(.+)\n1{1}$',re.M)
findall_str=re.findall(re_str,str)
findall_str.sort()

for num in findall_str:
    #print(num[0:3])
    Signid.append('201812300'+num[0:3])
'''
lenSignid=len(Signid)
print(lenSignid)
b=0   
for b in range(lenSignid-1):
    print(Signid[b]) 
    #print(type(Signid[b]))
'''

i=0
for Stuid in Studentid:
    if Stuid in Signid:
        i=i+1
    if Stuid not in Signid:
        print('学号'+Stuid+sheet.cell_value(i+6,1)+'未签到')
    