#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from __future__ import print_function
import threading
from socket import *


def conn_scan(host, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((host, port))
        print(host, port, 'is avaliable.')
    except Exception as e:
        print()
    finally:
        conn.close()


def main():
    threads = []
    host = "120.24.222.231"
    for port in range(20, 5000):
        thr = threading.Thread(target=conn_scan, args=(host, port))
        thr.start()
        threads.append(thr)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()

