__author__ = 'achandelkar'

'''
(S1+S1).substr(S2)
'''
def IsRotation(S1,S2):
    if len(S1) != len(S2):
        return False
    return S2 in S1+ S1


if __name__ == '__main__':
    S1 = eval(input("Enter the Input string ::"))
    S2 = eval(input("Enter the string which is to be checked if rotation of input string ::"))
    if IsRotation(S1,S2):
        print("{} is a rotation of {}".format(S2,S1))
    else:
        print("{} is not a rotation of {}".format(S2,S1))
