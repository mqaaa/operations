#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from __future__ import print_function
import threading
from queue import Queue


def test_thread(data, q):
    result = []
    for i in data:
        result.append(i * i)
    q.put(result)


def main():
    q = Queue()
    threads = []
    data = [[4, 2, 5], [4, 5, 6], [7, 8, 9], [8, 5, 2]]
    for i in range(4):
        thr = threading.Thread(target=test_thread, args=(data[i], q))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()

    result = []
    for i in range(4):
        result.append(q.get())
    print(result)


if __name__ == '__main__':
    main()

