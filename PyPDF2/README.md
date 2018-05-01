# 使用PdfFileReader读取PDF文件
```
import PyPDF2
reader = PyPDF2.PdfFileReader(open('redbook-5th-edition.pdf','rb'))
reader.getNumPages()
#获取PDF页数
reader.getIsEncrypted()
#PDF是否加密
page = reader.getPage(4)
#选择当前页
page.extractText()
#解析文件内容
reader.getDocumentInfo()
```
#使用PdfFileWriter创建PDF文件
```
import PyPDF2
reader = PyPDF2.PdfFileReader(open('redbook-5th-edition.pdf','rb'))
writer = PyPDF2.PdfFileWriter()
writer.addPage(reader.getPage(1))
writer.addPage(reader.getPage(3))
writer.getNumPages()
writer.encrypt('123456')
#加密
output = open('style.pdf','wb')
writer.write(output)
#将内容写入
output.close()
```
#修改PDF页面
```
import PyPDF2
reader = PyPDF2.PdfFileReader(open('redbook-5th-edition.pdf','rb'))
writer = PyPDF2.PdfFileWriter()
page = reader.getPage(0)
page.rotateClockwise(180)
#旋转180度
writer.addPage(page)
output = open('temp.pdf','wb')
writer.write(output)
output.close()
```
#添加水印
```
import PyPDF2
reader = PyPDF2.PdfFileReader(open('redbook-5th-edition.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('waterMark.pdf','rb'))
writer = PyPDF2.PdfFileWriter()
for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)
output = open('watermark_test.pdf','wb')
writer.write(output)
output.close()
```
#使用PdfFileMerger合并多个单元格
```
from __future__ import print_function
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

input1 = open('test1.pdf', 'rb')
input2 = open('test2.pdf', 'rb')
input3 = open('test3.pdf', 'rb')

# add the first 3 Page of input1 document to output
merger.append(fileobj=input1, pages=(0, 3))
# insert the first page of input2 into the output beginning after the
# second page
merger.merge(position=2, fileobj=input2, pages=(0, 1))
# append entire input3 document to the end of the outPut document
merger.append(input3)
# Write to an output PDF document
output = open('document_output.pdf', 'wb')
merger.write(output)
output.close()
```
