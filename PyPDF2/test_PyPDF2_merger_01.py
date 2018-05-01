#!/usr/bin/python
# _*_ coding: UTF-8 _*_
# 使用PdfFileMerger合并多个PDF文件

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

