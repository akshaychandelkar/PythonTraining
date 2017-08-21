__author__ = 'achandelkar'

def CompareTwoLists(L1,L2):
    if type(L1) != list or type(L2) != list:
        print("Input is not a list")
        return

    if len(L1) != len(L2):
        return 0
    L1.sort()
    L2.sort()
    for i in range (0,len(L1)):
        if L1[i] == L2[i]:
            continue
        break
    else:
        return 1
    return 0

if __name__ == '__main__':
    L1 = eval(input("Enter the first List for comparison::"))
    L2 = eval(input("Enter the Second List for comparison::"))
    res = CompareTwoLists(L1,L2)
    if res:
        print("The Lists are same")
    else:
        print("The Lists not are same")









