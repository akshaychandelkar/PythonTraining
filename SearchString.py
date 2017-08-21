__author__ = 'achandelkar'

def StringOccurence(S1,S2):
    count = 0
    i = 0
    while i != -1:
        i = S1.find(S2)
        if i != -1:
            count +=1
            S1 = S1[i+1:]
    return count


if __name__=='__main__':
    S1 = eval(input("Enter a string::"))
    S2 = eval(input("Enter the string to search::"))
    res = print(StringOccurence(S1,S2))

