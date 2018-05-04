#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from __future__ import print_function
import threading
import subprocess


def is_reacheable(ip):
    if subprocess.call(['ping', '-c', '2', ip]):
        print("{0} is alive.".format(ip))
    else:
        print("{0} is un unreacheable".format(ip))


def main():
    with open('ips.txt') as f:
        lines = f.readlines()
        threads = []
        for ip in lines:
            thr = threading.Thread(target=is_reacheable, args=(ip[:-1],))
            thr.start()
            threads.append(thr)
        for thr in threads:
            thr.join()


if __name__ == '__main__':
    main()

