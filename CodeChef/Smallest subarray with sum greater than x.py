A = [6, 3, 4, 5, 4, 3, 7, 9]
x = 16
start = 0
end = 0
current_sum = 0
minimum_length = len(A)

while len(A) > end != start:
    if current_sum <= x:
        current_sum += A[end]
        end += 1
    elif current_sum > x:
        if minimum_length > (end - start): minimum_length = (end - start)
        if end == len(A)-1:
            start += 1
            continue
        end += 1
        start += 1
print(start)
print(minimum_length)