#! /usr/bin/python
# coding=utf-8

from __future__ import print_function
def print99():
    n=1
    while n<=9:
        m=1
        while m<=n :
            print("%sx%s=%s"%(m,n,m*n),end="\t")
            m+=1
        print()
        n+=1

    for i in range(1,10):
        for j in range(1,i+1):
            print("{}x{}={}".format(j,i,j*i),end="\t")
        print()

print99()
#下周一中午13:30重庆字节跳动
#隔那么多天
