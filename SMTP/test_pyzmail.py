#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import imapclient
import pyzmail
imap = imapclient.IMAPClient('imap.qq.com', ssl=True)
imap.login('1163306125@qq.com', 'eanawsrirgcofhdb')
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




