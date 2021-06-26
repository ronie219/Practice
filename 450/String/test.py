arr = [1,1,1, 1]
queries = [1, 1, 2,1,2]
result = []
count = 0


for element in arr:
    if element == 1:
        count += 1
    else:
        break

end = len(arr) - 1


for query in queries:
    if end == -1: end = len(arr) - 1
    if query == 1 and count != len(arr):
        if arr[end] == 1:
            count += 1
        else:
            count = 0
        end -= 1
    elif query == 2:
        result.append(count)

print(arr)
print(result)
