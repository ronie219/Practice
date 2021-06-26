n,m=map(int,input().split())
a=[0]*(n+1)
m_sum=temp=0
for _ in range(m):
    f,l,val=[int(n) for n in input().split()]
    a[f-1]+=val
    if l<=n:
        a[l]-=val
for i in a:
    temp+=i
    if m_sum<temp:
        m_sum=temp
print(m_sum)  
