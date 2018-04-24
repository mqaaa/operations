#!/usr/bin/python
import time
import os
import random
for i in range(100):
	os.system("date>>test/"+str(random.randint(1,3))+".txt")
	time.sleep(0.5)
