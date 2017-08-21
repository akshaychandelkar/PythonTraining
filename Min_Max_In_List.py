__author__ = 'achandelkar'

def MaxMin(L1):
    Max = L1[0]
    Min = L1[0]
    i = 1
    while i < len(L1):
        if(L1[i] > Max):
            Max = L1[i]
        if(L1[i] < Min):
            Min = L1[i]
        i+=1
    return (Max,Min)

if __name__ == '__main__':
    L1 = eval(input("Enter a List to be reversed::"))
    print(MaxMin(L1))

