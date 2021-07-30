def binary_search(arr,left,right,key):
    if right>=left:
        mid = left+(right-left)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binary_search(arr,left,mid-1,key)
        else:
            return binary_search(arr,right,mid+1,key)
    else:
        return-1
arr = [1,2,3,4,5,6,7,8]
key = int(input())
res=binary_search(arr,0,len(arr)-1,key)
print(res)