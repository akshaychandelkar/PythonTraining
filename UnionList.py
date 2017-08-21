__author__ = 'achandelkar'
#!C:\Python34\python.exe

def Union(L1,L2):
    L3 = L1
    i = 0
    while i < len(L2):
        if L2[i] not in L3:
            L3.append(L2[i])
        i+=1
    return L3

def Intersection(L1,L2):
    L3 = []
    i = 0
    while i < len(L2):
        if L2[i] in L1:
            L3.append(L2[i])
        i+=1
    return L3

def InvIntersection(L1,L2):
    L3 = []
    i = 0
    while i < len(L2):
        if L2[i] not in L1:
            L3.append(L2[i])
        else:
            L1.remove(L2[i])
        i+=1
    L3.extend(L1)
    return L3

if __name__ == '__main__':
    L1 = eval(input("Enter the first List for comparison::"))
    L2 = eval(input("Enter the Second List for comparison::"))
    #res = Union(L1,L2)
    #res1 = Intersection(L1,L2)
    res2 = InvIntersection(L1,L2)
    #print("The Union of Lists :: {0} ".format(res))
    #print("The Intersection of Lists :: {0} ".format(res1))
    print("The Inverse Intersection of Lists :: {0} ".format(res2))
