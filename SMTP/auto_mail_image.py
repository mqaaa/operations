#!/usr/bin/python
# _*_ codingL UTF-8 _*_
from __future__ import print_function
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
msg['From'] = me
msg['to'] = COMMASPACE.join(family)
msg.preamble = 'Our family reunion'
for file in pngfiles:
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

s = smtplib.SMTP('localhost')
s.sendmail('1163306125@qq.com',
           ['qmeng1128@163.com',
            '15735184252@163.com'],
           msg.as_string())
s.quit()

