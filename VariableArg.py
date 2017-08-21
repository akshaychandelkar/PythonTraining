__author__ = 'achandelkar'
#!C:\Python27\python.exe

def VariableArgAdd(*args):
    print(type(args))
    for x in args:
        print(x)
VariableArgAdd(1,2,3)
print(VariableArgAdd())
VariableArgAdd(1,2,3,4,5,6,7,8,9)
print(VariableArgAdd())