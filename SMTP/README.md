# SMTP
## smtplib发送邮件
```
import smtplib
smtp = smtplib.SMTP('smtp.qq.com',25)
smtp.ehlo()
smtp.starttls()
smtp.login('1163306125@qq.com','eanawsrirgcofhdb')
smtp.sendmail('1163306125@qq.com','15735184252@163.com','Subject: this is a title \n this is content')
smtp.quit()

```
## MIMEText
```
#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from __future__ import print_function
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 25


def send_mail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    print('Connecting To Mail Server.')
    try:
        smtp_server.ehlo()
        print('Starting Encrypted Section.')
        smtp_server.starttls()
        smtp_server.ehlo()
        print('Logging Into Mail Server')
        smtp_server.login(user, pwd)
        print('Sending Mail.')
        smtp_server.sendmail(user, to, msg.as_string())
    except Exception as err:
        print('Sending Mail Failed:{0}'.format(err))
    finally:
        smtp_server.quit()


def main():
    send_mail(
        '1163306125@qq.com',
        'xxxxxxxxx',
        'yourEmail',
        'Important',
        'Test Message')


if __name__ == '__main__':
    main()

```
## MIMEImage
```
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

```
## yagmail
```
import yagmail
with yagmail.SMTP(user=user,password=password,host=host,port=25/465) as yag:
    yag.send(recipients,subject,content)
``` 
## 接收邮件
```
import imapclient
imap = imapclient.IMAPClient('imap.qq.com',ssl=True)
imap.login('1163306125@qq.com','eanawsrirgcofhdb')
imap.list_folders()
imap.select_folder(u'INBOX')
uids = imap.search(['ALL'])
uids
raw_message = imap.fetch(362,['BODY[]'])

```
## pyzmail解析邮件
```
#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import imapclient
import pyzmail
imap = imapclient.IMAPClient('imap.qq.com', ssl=True)
imap.login('1163306125@qq.com', 'cofhdb')
imap.list_folders()
imap.select_folder('INBOX', readonly=True)
imap.search(['ON 05-Jul-2017'])
imap.search(['SINCE 01-Jul-2017', 'BEFORE 05-Jul-2017'])
UIDS = []
UIDS = imap.search(['all'])
rew_message = imap.fetch(UIDS[0], ['BODY[]'])
imap.select_folder('INBOX', readonly=False)
print(rew_message[UIDS[0]][b'BODY[]'])
message = pyzmail.PyzMessage.factory(rew_message[UIDS[0]][b'BODY[]'])
print(message.get_address('from'))
print(message.get_address('to'))
print(message.get_address('cc'))
print(message.get_subject())

```
## 删除邮件
```
imap.delete_messages(uids)
imap.expunge()
```
