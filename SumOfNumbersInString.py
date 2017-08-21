__author__ = 'achandelkar'

def SumOfDigits(S1):
    Sum = 0
    i = 0
    while i < len(S1):
        if S1[i].isnumeric():
            Sum+= int(S1[i])
        i+=1
    return Sum

if __name__ == '__main__':
    S1 = eval(input("Enter an alphanumeric string ::"))
    res = SumOfDigits(S1)
    print("The sum of digits in the alpha numeric string is :: {0}".format(res))