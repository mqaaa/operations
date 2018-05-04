# 网络
## 1.1 列出网络上所有的活动主机
```
$ping www.baidu.com 
```

我们可以引入多线程,来解决网络延时的问题

```
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
```
## 1.2 端口扫描
### 1.2.1 简单办法，就是使用socket

```
import socket
s = socket.socket()
s.connect(('120.24.222.231', 80))
```

我们依旧可以使用多线程去处理

```
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

```

**还有一个小技巧**
就是列表推导

```
In [1]: from itertools import product

In [2]: a = ('a','b','c')

In [3]: b = (1,2)

In [4]: list(product(a,b))
Out[4]: [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]

In [5]: list([(x,y) for x in a for y in b])
Out[5]: [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]

```

### 1.2.2 上工具 nmap（Network Mapper）
* https://nmap.org/dist/nmap-7.70-1.src.rpm
```
nmap 120.24.222.231 #端口侦测
nmap -sV 120.24.222.231 #侦测版本
nmap -sO 120.24.222.231 #侦测系统
```
```
In [1]: import nmap

In [2]: nm = nmap.PortScanner()

In [3]: nm.scan('wwww.baidu.com','22-1000')
Out[3]: 
{'nmap': {'command_line': 'nmap -oX - -p 22-1000 -sV wwww.baidu.com',
  'scaninfo': {'tcp': {'method': 'syn', 'services': '22-1000'}},
  'scanstats': {'downhosts': '0',
   'elapsed': '25.06',
     **************
     'reason': 'syn-ack',
     'state': 'open',
     'version': ''}},
   'vendor': {}}}}


```
## 使用Ipy进行IP地址管理
```
wantprefixlen == 0 / None     don't return anything（只返回一个IP地址）   1.2.3.0
wantprefixlen == 1            /prefix                1.2.3.0/24
wantprefixlen == 2            /netmask                1.2.3.0/255.255.255.0
wantprefixlen == 3            -lastip （）                1.2.3.0-1.2.3.255

>>> IP('192.168.1.0/24').strNormal(0)
'192.168.1.0'
>>> IP('192.168.1.0/24').strNormal(1)
'192.168.1.0/24'
>>> IP('192.168.1.0/24').strNormal(2)
'192.168.1.0/255.255.255.0'
>>> IP('192.168.1.0/24').strNormal(3)
'192.168.1.0-192.168.1.255'
``` 

```
判断IP地址和网段是否在另一个网段中 
IP类可以支持类似数值的比较

>>> '192.168.1.100' in IP('192.168.1.0/24')
True
```
- reverseNames() 返回IP的反向地址解析模式 
- iptype() 返回IP地址的类型 
- int() 将IP地址转换为整数格式 
- strHex() 将IP地址转换为16进制格式 
- strBin() 将IP地址转换为二进制格式 
- net() 输出其网络地址 
- netmask() 输出其网络掩码

## 使用dnspython解析DNS
* http://www.dnspython.org/
## 网络嗅探器Scapy
* https://scapy.net/
```
