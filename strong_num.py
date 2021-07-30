def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
def strong(num):
    s = 0
    while(num != 0):
        remainder = num % 10
        s = (s) + fact(remainder)
        num = num // 10
    if(k==s):
        print("the num is strong")
    else:
        print("not strong")
num = int(input())
k = num
strong(num)
