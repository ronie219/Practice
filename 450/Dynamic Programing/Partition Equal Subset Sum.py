# recursive
def subsetSum_r(arr):
    total = sum(arr)
    if total % 2 == 1:
        return False

    target = total // 2

    memo = {}

    def _solve(target, arr):
        if target == 0:
            return True
        if not arr:
            return False
        # if target in memo.keys():
        #     return memo[target]
        # we have two option take it or leave it.

        # take
        option1 = False
        option2 = False
        if target - arr[0] >= 0:
            option1 = _solve(target - arr[0], arr[1:])
        option2 = _solve(target, arr[1:])

        # memo[target] = option1 or option2
        return option1 or option2

    return _solve(target, arr)


# itterative


def subsetSum_i(N, arr):
    total = sum(arr)
    if total % 2 == 1:
        return False

    target = total // 2
    dp = [[None for i in range(target + 1)] for j in range(N + 1)]

    # we cannot make any target with empty subset so we isilize with False
    for i in range(len(dp[0])):
        dp[0][i] = False

    for i in range(len(dp)):
        dp[i][0] = True

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if col - arr[row - 1] >= 0:
                dp[row][col] = dp[row - 1][col] or dp[row - 1][col - arr[row - 1]]
            else:
                dp[row][col] = dp[row - 1][col]

    return dp[-1][-1]


if __name__ == "__main__":
    N = 4
    arr = [1, 5, 11, 5]
    print(subsetSum_i(N, arr))
    print(subsetSum_r(arr))
