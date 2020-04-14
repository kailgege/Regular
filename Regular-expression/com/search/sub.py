import re
import urllib.request 
import urllib 
url = 'http://www.cntour.cn/'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
htmldata = response.read() 
htmldata = htmldata.decode('utf-8')
#print(htmldata)

re_a=re.compile(r"<a.*?</a>")
re_url=re.compile(r"http[s]?.*?[\"|\']")
findall_url=re.findall(re_a,htmldata)
print("所有原网页中的连接")
for i in findall_url:
    k=re.findall(re_url,i)
    for j in k:
        h=re.sub("[\"|\']","",j)
        print(h)     

re_img=re.compile(r"<img.*?>")
re_src=re.compile(r"src\=\".*?\"")
findall_url=re.findall(re_img,htmldata)
print("所有原网页图片来源")
for i in findall_url:
    k=re.findall(re_src,i)
    for j in k:
        print(j)   
