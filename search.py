def search(arr,key,n):
    arr1 = []
    flag = False
    for i in range(n):
        if(key==arr[i]):
            flag = True
            arr1.append(int(input()))
    if flag == True:
        print("element is found")
        for i in arr1:
            print(i)
    else:
        print("key is not found")
arr =int(input())
n=len(arr)
key = int(input())
search(arr,key,n)