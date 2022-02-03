def lcs(string1, string2):
    memo = {}

    def _solve(s1, s2, n, m):

        # base case
        if n < 0 or m < 0:
            return 0

        if (n, m) in memo.keys():
            return memo[(n, m)]

        # if the last char is equal
        if s1[n] == s2[m]:
            memo[(n, m)] = _solve(s1, s2, n - 1, m - 1) + 1
            return memo[(n, m)]

        # if last cahr is not equal
        else:
            memo[(n, m)] = max(_solve(s1, s2, n - 1, m), _solve(s1, s2, n, m - 1))
            return memo[(n, m)]

    print("*" * 50)
    return _solve(string1, string2, len(string1) - 1, len(string2) - 1)


def lcs(x, y, s1, s2):
    dp = [[None for _ in range(y + 1)] for __ in range(x + 1)]

    # we insilize the border with zero which mean longest substring with _ to _ which is 0
    for row in range(len(dp)):
        dp[row][0] = 0
    for col in range(len(dp[0])):
        dp[0][col] = 0

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if s1[row - 1] == s2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    print(dp)
    return dp[-1][-1]


def lcs(x, y, s1, s2):
    prev = [0 for _ in range(x + 1)]
    current = [0 for _ in range(x + 1)]

    for s1idx in range(len(s1)):
        for s2idx in range(len(s2)):
            if s1[s1idx] == s2[s2idx]:
                current[s1idx + 1] = prev[s1idx]
            else:
                current[s1idx + 1] = max(prev[s1idx + 1], current[s1idx])
            prev = current
    print(current)


if __name__ == "__main__":

    a = "ABCDGAcHACsAmndsldfslnlksdfj"
    b = "AEDFHRfdslkjhfdosljgpdsig[ffdipojgffjdd[gfjdpojh"

    print(lcs(len(a), len(b), a, b))
