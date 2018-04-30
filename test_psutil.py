#!/usr/bin/python
#_*_ coding: UTF-8 _*_
from __future__ import print_function
import psutil
import datetime

print("psutil.cpu_count()|逻辑CPU:{0}".format(psutil.cpu_count()))
print("psutil.cpu_count(logical=False)|物理CPU:{0}".format(psutil.cpu_count(logical=False)))
print("psutil.cpu_percent()|CPU利用率{0}".format(psutil.cpu_percent()))
print("psutil.cpu_percent(percpu=True)|单个CPU利用率{0}".format(psutil.cpu_percent(percpu=True)))
print("psutil.cpu_percent(interval=2,percpu=True)|指定时间范围CPU利用率{0}".format(psutil.cpu_percent(interval=2,percpu=True)))
print("psutil.cpu_times()|返回CPU的时间花费",end="")
scputimes = psutil.cpu_times()
list(scputimes)
print(scputimes)
print("psutil.cpu_times_percent()|返回CPU的时间花费的比例",end="")
scputimes = psutil.cpu_times()
list(scputimes)
print(scputimes)
print("psutil.cpu_stats()|返回CPU的统计信息:",end="")
print(list(psutil.cpu_stats()))
