def pow(base,expo):
    if(expo==0):
        return 1
    result = base
    increment = expo
    for i in range(1,base):
        for j in range(1,expo):
            result += expo
        increment = result
    return result
base = int(input())
expo = int(input())
print(pow(base,expo))
