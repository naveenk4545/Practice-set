first = int(input())
second = int(input())
for i in range(first,second):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)