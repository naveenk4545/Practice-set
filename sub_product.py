def subarray(arr,n):
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i+n,n):
            result = max(result,mul)
            mul *= arr[j]
        result = max(result,mul)
    return result
arr = [1,-2,-3,4,5,-6]
n = len(arr)
print(subarray(arr,n))