#!/usr/bin/python
#_*_ coding: UTF-8 _*_
import sys
import os
import fnmatch
import tarfile
import datetime

def is_find_match(filename,patterns):
	for pattern in patterns:
		if fnmatch.fnmatch(filename,pattern):
			return True
	return False

def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
	for root,dirnames,filenames in os.walk(root):
		for filename in filenames:
			if is_find_match(filename,patterns):
				yield os.path.join(root,filename)
		for dirname in dirnames:
			if dirname in exclude_dirs:
				dirnames.remove(dirname)

def main():
	patterns = ['*.py','*.log','*.cnf']
	now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	filename = "all_py_{0}.tar.gz".format(now)
	with tarfile.open(filename,'w:gz') as f:
		for item in find_specific_files(".",patterns):
			f.add(item)

if __name__ == '__main__':
	main()

