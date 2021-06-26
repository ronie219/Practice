arr = [1, 5, 8, 10]
k = 2
N = 4
arr.sort()
ans = arr[-1] - arr[0]
smallest = arr[0] + k
largest = arr[-1] - k
for i in range(N-1):
    mi = min(smallest,arr[i+1]-k)
    mx = max(largest, arr[i] + k)
    if mi < 0:
        continue
    ans = min(ans, mx-mi)
print(ans)
