__author__ = 'achandelkar'
#!C:\Python27\python.exe

def Add(a,b):
    print(a,b)
    return a+b
res = Add(10,20)
print(res)
res = Add(b=10,a=20)
print(res)

def Add(a,b,c=20):
    return a+b+c
res = Add(10,10)
print(res)
res = Add(10,b=30)
print(res)
res = Add(b=10,a=20)
print(res)
res = Add(1,c=200,b=100)
print(res)
res = Add(1,b=30,c=100)
print(res)

