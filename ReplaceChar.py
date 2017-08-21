__author__ = 'achandelkar'

'''
def ReplaceFirstCharOccurences(S1,ReplaceBy):
        return S1[0] + S1[1:].replace(S1[0],ReplaceBy)
'''
def ReplaceFirstCharOccurences(S1,ReplaceBy):
    S2 = S1[0]
    ch = S1[0]
    i = 1
    while i < len(S1):
        if S1[i] == ch:
            S2+=ReplaceBy
        else:
            S2+=S1[i]
        i+=1
    return S2




if __name__ == '__main__':
    S1 = eval(input("Enter a string::"))
    ReplaceBy = eval(input("Enter the char to be replaced by::"))
    res = ReplaceFirstCharOccurences(S1,ReplaceBy)
    print("The new string is :: {0}".format(res))