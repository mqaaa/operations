#!/usr/bin/python
# _*_ coding: UTF-8 _*_
#只能发送文本
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

