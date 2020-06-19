# No Idea!

mn = map(int,input().split())
inarray = list(map(int,input().split()))
Aset = set(map(int,input().split()))
Bset = set(map(int,input().split()))
print(sum((i in Aset)- (i in Bset) for i in inarray))