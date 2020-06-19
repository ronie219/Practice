# Ciel and A-B Problem
a,b = map(int,input().split())
if int(a - b) % 10 == 9:
    print((a - b)+1)
else:
    print((a - b) + 1)
