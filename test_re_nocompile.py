#!/usr/bin/python
# _*_ codeing: UTF-8 _*_
from __future__ import print_function
import re
import time

def main():
	time_start = time.time()
	pattern = "[0-9]+"
	with open('test/1.txt') as f:
		for line in f:
			print(re.findall(pattern,line))
	time_end = time.time()
	#print('{:_^+10.4f}'.format(time_end-time_start))
	print(": {:_^+10.4f}".format(3.1415926))

if __name__ == '__main__':
	main()
