#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

setup(
    name='emaili',
    version='0.2',
    author='Qmeng',
    author_email='1163306125@qq.com',
    url='https://github.com/mqaaa/operations/emaili',
    description='A email client in terminal',
    packages=['emaili'],
    install_requires=['yagmail'],
    tests_require=['nose', 'tox'],
    entry_points={
        'console_scripts': [
            'emaili=emaili:main',
        ]
    }
)
