#!/usr/bin/python
#_*_ coding: UTF-8 _*_
from __future__ import print_function
import os
import sys
import fnmatch

def is_find_match(filename,parrerns):
	for pattern in patterns:
		if fnmatch.fnmatch(filename,pattern):
			return True
		return False 

def is_specific_files(root='.',patterns='[*]',exclude_dirs=[]):
	for root,dirnames,filenames in os.walk(root):
		for filename in filenames:
			if is_find_match(filename,patterns):
				yield os.path.join(root,filename)
		for dirname in exclude_dirs:
			if dirname in dirnames:
				dirnames.remove(dirname)

if __name__ == '__main__':
	root = input('遍历的文件夹:')
	key = input('1.最大的十个文件\n2.最老的十个文件\n3.文件名包含指定字符的文件\n4.除git下的py文文件')
	if key == 1:
		file_size = { name: os.path.getsize(name) for name in is_specific_files(root) }
		result = sorted(file_size.items(),key=lambda d:d[1],reverse=True)[:10]
		for i,t in enumerate(result,1):
			print(i,t[0],t[1])
	else if k == 2:
		file_age = { name:os.path.getmtim(name) for name in is_specific_files(root)}
		result = sorted(file_age.items(),key=lambda d:d[1])[:10]
		for i,t in enumerate(result,1):
			print(i,t[0],t[1])
	else if k == 3:
		files = [name for name in is_specific_files('.', patterns=['*mysql-bin*'])]
		for i,name in enumerate(files,1):
			print(i,name)
	else:
		files = [name for name in is_specific_files('.', patterns=['*.py'],exclude_dirs= ['.git'])]
		for i,name in enumerate(files,1):
			print(i,name) 
