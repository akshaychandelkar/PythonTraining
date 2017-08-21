__author__ = 'achandelkar'
#!C:\Python27\python.exe

def add(a,b):
    return a + b
res = add(10,20) #Positional argument
print("The value of res is :%d"%res)

def add(a,b=10):
    return a + b
res = add(100,200)
print(res)
res = add(100) #Default argument
print(res)

def sub(a=20,b=10):
    return a - b
res = sub()
print(res)