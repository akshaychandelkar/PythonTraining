__author__ = 'achandelkar'
#!C:\Python27\python.exe

def Add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

res = Add(10,20,30)
print(res)
res = Add(20,40,70,80)
print(res)
