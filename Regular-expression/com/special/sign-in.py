import re
import xlrd 

Studentid=[]
Signid=[]

wb=xlrd.open_workbook(u'data/ZX2300398101-20200310_二班学生.xlsx')
sheet=wb.sheet_by_index(0)

rows=sheet.nrows
for i in range(6,rows):
    Studentid.append(sheet.cell_value(i,0).strip())

with open('data/2.txt','r') as f:
   str=f.read() 

re_str=re.compile(r'^(.+)\n1{1}$',re.M)
findall_str=re.findall(re_str,str)
findall_str.sort()

for num in findall_str:
    num.encode('utf-8')
    #print(num[3:])
    if num[0:3]=='080':
        if num[3:]=='农成兴':
            Signid.append('201712300'+num[0:3])
    else:
        Signid.append('201812300'+num[0:3])

i=0
for Stuid in Studentid:
    if Stuid in Signid:
        i=i+1
    if Stuid not in Signid:
        print('学号'+Stuid+sheet.cell_value(i+6,1)+'未签到')  