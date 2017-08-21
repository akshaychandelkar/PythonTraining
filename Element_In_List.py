__author__ = 'achandelkar'
#!C:\Python34\python.exe

def Count(L1,key):
    count = 0
    for x in L1:
        if key == x:
            count+=1
    return count

if __name__ == '__main__':
    L1 = eval(input("Enter a list::"))
    key = eval(input("Enter the character to be counted::"))
    print(Count(L1,key))



