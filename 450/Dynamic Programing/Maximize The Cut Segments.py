# recurrsion + memo
# def maximizeTheCuts(n, x, y, z):
#     meme = {}

#     def _solve(n):
#         # base case
#         if n == 0:
#             return 0
#         if n in meme.keys():
#             return meme[n]
#         count = 0
#         for cut in (x, y, z):
#             if n - cut >= 0:
#                 var = _solve(n - cut) + 1
#                 if count < var:
#                     count = var
#         meme[n] = count
#         return count

#     print(_solve(n))
def maximizeTheCuts(n, x, y, z):
    dp = [None for _ in range(n + 1)]
    dp[0] = 0

    for idx in range(1, len(dp)):
        max_value = float("-inf")
        for cut in (x, y, z):
            if idx - cut >= 0:
                if dp[idx - cut] > max_value:
                    max_value = dp[idx - cut]

        dp[idx] = max_value + 1
    print(dp[-1])


if __name__ == "__main__":
    maximizeTheCuts(10000, 800, 3000, 5000)  # 12
    maximizeTheCuts(7, 8, 2, 5)  # 12
