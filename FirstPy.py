#!/usr/bin/python
#-*-coding:utf-8 -*-
# print("hello world...")
#python第一天
# print("你好, 世界...")
# a=3
# if(a>0):
#     print("我是好人...")
# else:
#     print("我是坏人...")
# a=b=c=11
# print(c)
# a,b,c=1,"我爱中国",11.33
# print(b);print(a);print(c)
#字符串拼接
# str1='a'
# str2="b"
# str3="cd"
# str=str1+\
#     str2+\
#     str3
# print(str)
for i in range(1,10):
    for j in range(1,i+1):
        print "%d*%d=%2d"%(i,j,i*j),
    print ("")