def longIncrSub(arr):
    n = len(arr)
    sub = [1] * n  

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                sub[i] = max(sub[i], sub[j] + 1)

    if sub:
        return max(sub)
    else:
        return 0


# Example
a=arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longIncrSub(a))