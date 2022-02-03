from collections import defaultdict


def LCSof3(A, B, C, n1, n2, n3):
    memo = defaultdict(int)

    def _solve(A, B, C, n1, n2, n3):
        if n1 < 0 or n2 < 0 or n3 < 0:
            return 0

        if (n1, n2, n3) in memo.keys():
            return memo[(n1, n2, n3)]

        if A[n1] == B[n2] == C[n3]:
            ans = _solve(A, B, C, n1 - 1, n2 - 1, n3 - 1) + 1
            memo[(n1, n2, n3)] = ans
            return ans

        else:
            ans = []
            ans.append(_solve(A, B, C, n1 - 1, n2, n3))
            ans.append(_solve(A, B, C, n1, n2 - 1, n3))
            ans.append(_solve(A, B, C, n1, n2, n3 - 1))
            ans.append(_solve(A, B, C, n1 - 1, n2 - 1, n3))
            ans.append(_solve(A, B, C, n1 - 1, n2, n3 - 1))
            ans.append(_solve(A, B, C, n1, n2 - 1, n3 - 1))

        memo[(n1, n2, n3)] = max(ans)
        return memo[(n1, n2, n3)]

    return _solve(A, B, C, n1, n2, n3)


def LCSof3(A, B, C, n1, n2, n3):
    dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for ___ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif A[i - 1] == B[j - 1] == C[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i - 1][j - 1][k],
                        dp[i - 1][j][k - 1],
                        dp[i][j - 1][k],
                        dp[i][j - 1][k - 1],
                        dp[i][j][k - 1],
                    )
    print(dp[-1][-1][-1])


if __name__ == "__main__":
    A = "geeks"
    B = "geeksfor"
    C = "geeksforgeeks"
    print(LCSof3(A, B, C, len(A) - 1, len(B) - 1, len(C) - 1))
