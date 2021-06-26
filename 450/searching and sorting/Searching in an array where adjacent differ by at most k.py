def search(arr,n,x,k):
    start = 0
    while start < n:
        if arr[start] == x:
            return start
        start = start + max(1,abs(arr[start]-x) // k)

    return -1


arr = [2, 4, 5, 7, 7, 6]
x = 10
k = 2
n = len(arr)
print("Element", x, "is present at index",search(arr, n, x, k))
