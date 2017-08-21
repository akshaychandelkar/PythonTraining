__author__ = 'achandelkar'
#!C:\Python34\python.exe
print("Its fun", __name__)
def SumOfEvenOdd(lb , ub):
    sum_even = 0
    sum_odd = 0
    while lb <= ub:
        if lb % 2 == 0:
            sum_even += lb
        else:
            sum_odd += lb
        lb +=1
    return sum_even,sum_odd

if __name__ == '__main__':
    lb,ub = input("Enter lower and upper bound numbers:")
    r1,r2 = SumOfEvenOdd(lb,ub)
    #print("The sum of even numbers is:%d"%r1)
    #print("the sum of odd numbers is :%d"%r2)
    print(r1,r2)