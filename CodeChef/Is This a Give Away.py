# Is This a Give Away
for _ in range(int(input())):
    l, r, k = map(int,input().split())
    print((r-l +1) if (r - l+1) < k else k)