#!/usr/bin/python
# _*_ coding: UTF-8 _*_
# 使用paramik部署监控程序
from __future__ import print_function
import paramiko

HOST = '120.24.222.231'
PASSWORD = '......'
PORT = 22
USERNAME = 'root'


def depoly_monitor(ip):
    with paramiko.SSHClient() as Client:
        Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            Client.connect(ip, PORT, USERNAME, PASSWORD)
        except Exception as e:
            raise SystemExit(e)
        stdin, stdout, stderr = Client.exec_command('ls -l')
        print(stdout.readlines())
        with Client.open_sftp() as sftp:
            sftp.put('test.py', 'test.py')
            sftp.chmod('test.py', 0o755)


def main():
    with open('ips.txt') as f:
        for line in f:
            depoly_monitor(line.strip())


if __name__ == '__main__':
    main()

