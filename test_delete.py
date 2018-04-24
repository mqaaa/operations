#!/usr/bin/python
#  _*_ coding:utf-8 _*_
from __future__ import print_function
import os
import sys
import time


def func(path):
    for it in os.listdir(path):
        if(it.endswith('.txt')):
            t = os.path.join(path, it)
            print("正在删除 " + t, end="")
            os.system("rm -rf " + t)
	    time.sleep(0.5)
            print(" OK")


if __name__ == '__main__':
	path = sys.argv[1]
	func(path)
