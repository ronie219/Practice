n = 2
dp = [0] * (n + 1)
result = {}
for i in range(1,n+1):
    dp[i]=dp[i>>1]+i%2
print(dp)
