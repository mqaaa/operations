#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import yagmail
yag = yagmail.SMTP(
    user='1163306125@qq.com',
    password='hdb',
    host='smtp.qq.com',
    port=465)
content = [ 
    'This mail come from yagmail',
    'This is a bodym and here is jest text',
    'You can find an image file and a pdf file attached.',
    'redbook-5th-edition.pdf',
    'README.md']
yag.send(
    '15735184252@163.com',
    'test',
    content)
yag.close()
