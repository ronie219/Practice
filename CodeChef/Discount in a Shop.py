
# Discount in a Shop
for _ in range(int(input())):
    N = input()
    ls = []
    for i in range(len(N)):
        ls=ls+[int(N[:i]+N[i+1:])]
    print(min(ls))
