N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]
A.sort()
minimum = A[-1] - A[0]
start = 0
end = M-1
# print(A)
while end < N:
    if A[end] - A[start] < minimum: minimum = A[end] - A[start]
    end += 1
    start += 1

print(minimum)