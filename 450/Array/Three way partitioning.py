n = 5
A = [1, 2, 3, 3, 4]
a, b = 1, 2

left = 0
right = n - 1
start = 0
while start < right:
    if A[start] < a:
        A[start],A[left] = A[left],A[start]
        left += 1
    elif A[start] > b:
        A[start], A[right] = A[right], A[start]
        right -= 1
    start += 1
print(A)