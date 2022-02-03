def catalan(num):

    dp = [None for _ in range(num + 1)]
    dp[0] = 1
    dp[1] = 1


    for fidx in range(2, num+1):
        start = 0
        end = fidx - 1
        solve = 0
        while start < fidx or end >= 0:
            solve += dp[start] * dp[end]
            start += 1
            end -= 1
        dp[fidx] = solve
    print(dp)

        




if __name__ == '__main__':
    """
    C0 = 1
    c1 = 1
    c2 = c1.c0 + c1.c0
    c3 = c0.c2 + c1.c1 + c2.c0
    """

    catalan(10)