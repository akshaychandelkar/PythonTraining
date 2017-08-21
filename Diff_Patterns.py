__author__ = 'achandelkar'
#!C:\Python34\python.exe


def Pattern1(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print ("\t",end='')
        for j in range(0,2*i+1):
            print ("*\t", end='')
        print ("\n")

def Pattern2(n):
    for i in range(0,n):
        for j in range(0,i):
            print ("\t",end='')
        for j in range(0,2*(n-i-1)+1):
            print ("*\t", end='')
        print ("\n")

def Pattern4(char,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print ("\t",end='')
        for j in range(0,2*i+1):
            print ("\t"%char, end='')
        print ("\n")

def main():
    n = eval(input("Enter the number of rows::"))

    #Pattern1(n)
    #Pattern2(n)
    Pattern4(n)



if __name__ == '__main__':
    main()