#!/usr/bin/python
from __future__ import print_function
import os
import sys
from collections import Counter

def func():
	c = Counter()
	with open(os.path.expanduser('~/.bash_history')) as f:
		for line in f:
			cmd = line.strip().split()
			if cmd:
				c[cmd[0]]+=1
	print(c.most_common(10))

if __name__ == '__main__':
	func()
