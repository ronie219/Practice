string = '0100110101'

count1 = 0
count0 = 0
count = 0
for i in string:
    if i == '0':
        count0 += 1
    else:
        count1 += 1
    if count0 == count1:
        count += 1

if count1 != count0:
    print(-1)
else:
    print(count)
