
# ginortS
S = input()
up = ''
low = ''
odd = ''
even = ''
for i in S:
    if i.islower():
        low += i
    if i.isupper():
        up += i
    if i.isdigit():
        if int(i) % 2 == 1:
            odd += i
        else:
            even += i
result = (sorted(low) + sorted(up) + sorted(odd) + sorted(even))
print((''.join([i for i in result])))