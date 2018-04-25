#!/usr/local/python
# _*_ coding: UTF-8 _*_
form __future__ import print_function
from collections import Counter
import sys
__PATH__ = sys.argv[1]
print(__PATH__)
c = Counter()
with open(__PATH__) as f:
    for line in f:
        c[line.split()[6]] += 1
print("{0}".format(c.most_common(1)))
