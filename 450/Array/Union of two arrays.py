# 5 3
# 1 2 3 4 5
# 1 2 3

# 6 5
# 1 1 2 2 3 3
# 8 9 7 6 5
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i = 0
j = 0
output = 0
current_value = None
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        output += 1 if a[i] != current_value else 0
        current_value = a[i]
        i += 1
    elif a[j] < b[i]:
        output += 1 if b[j] != current_value else 0
        current_value = b[j]
        j += 1
    else:
        i += 1
        j += 1
        output += 1
if i < len(a):
    for p in range(i,len(a)):
        output += 1 if current_value != a[p] else 0
elif j < len(b):
    for q in range(j, len(b)):
        output += 1 if current_value != b[q] else 0

print(output)
