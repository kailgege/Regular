'''
Created on 2019年11月14日

@author: 13476
'''
'''
import os
print(os.path.abspath('TestDir/dir2/doc22.docx'))
'''
import docx
from docx import Document
path = "C:\\Users\\13476\\Desktop\\word.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)