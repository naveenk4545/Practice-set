def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if(num%i==0):
            sum = sum+i
    if(num==sum):
        print("this is perfect num")
    else:
        print("this is not perfect num")
num =  int(input())
perfect_num(num)