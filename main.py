import math
def checkNum():
    a = 2
    if(a<0):
       print("The given number is Negative: ", a)
    elif(a==0):
        print("The given number is zero: ", a)
    else:
        print("The given number is positive: ", a)
def checkOddOrEven():
    a = 2
    if(a%2 == 0):
        print("The given number is even")
    else:
        print("The given number is odd")
def checkLargestNum():
    a = 1
    b = 2
    c = 3
    if(a>b and a>c):
        print("A is grater than other")
    elif(b>a and b>c):
        print("b is grater than other")
    else:
        print("C is grater than other")
def checkPrime():
    a = 12
    for i in range(2,math.ceil(a/2)):
        if(a%i == 0):
            print("The given no is not prime")
            break
    else:
        print("The given no is prime")
def findFactorial():
    a = 6
    fac = 1
    for i in range(1,a):
        fac = fac*i
    print("The factorail of the number is: ", fac)
def giveMultiplication():
    a = 10
    for i in range(1,11):
        print(a ,"*", i ,"=", a*i)
def findSumOfNaturalNos():
    a =11
    sum = 0
    for i in range(1,a):
        sum = sum + i
    print("The Sum Of natural Number is: ", sum)
def findFibonacci():
    a = 0
    b = 1
    print(a)
    for i in range(1, 11):
        c = a+b
        a = b
        b = c
        print(a)
def findArmstrongNum():
    print("Find Armstrong numbers:")
    low = 100
    high = 2000
    for num in range(low, high+1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp>0:
            digit = temp%10
            sum += digit**order
            temp //= 10
        if num == sum:
            print(num)
def findprimeNumbers():
    print("Find Prime numbers:")
    low =1
    high =100
    for num in range(low,high+1):
        if num>1:
            for i in range(2, num):
                if (num %i) == 0:
                    break
            else:
                print(num)

checkNum()
checkOddOrEven()
checkLargestNum()
checkPrime()
findFactorial()
giveMultiplication()
findSumOfNaturalNos()
findFibonacci()
findArmstrongNum()
findprimeNumbers()
