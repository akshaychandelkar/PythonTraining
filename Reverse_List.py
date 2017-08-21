__author__ = 'achandelkar'

def ReverseList(L1):
    L2 = []
    i = len(L1)
    while i > 0:
        L2.append(L1[i-1])
        i -=1
    return L2

if __name__ == '__main__':
    L1 = eval(input("Enter a List to be reversed::"))
    res = ReverseList(L1)
    print("The reverse list is:: {0}".format(res))

