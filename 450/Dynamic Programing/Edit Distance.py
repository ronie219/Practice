def distance_r(s1, s2):
    memo = {}

    def _solve(src, target):

        # base case
        if src == "" and target == "":
            return 0

        # if we have same value at the 1st char of both string then we do nothing
        if (src, target) in memo.keys():
            return memo[(src, target)]

        if src and target:
            if src[0] == target[0]:

                memo[(src, target)] = _solve(src[1:], target[1:])
                return memo[(src, target)]

        # if both the charter is different then we can do three operation
        # insert, delete, replace and return the min
        insert, replace, delete = float("inf"), float("inf"), float("inf")

        if target:
            insert = _solve(src, target[1:])

        if src and target:
            replace = _solve(src[1:], target[1:])

        if src:
            delete = _solve(src[1:], target)
        memo[(src, target)] = min(insert, delete, replace) + 1
        return memo[(src, target)]

    print(_solve(s1, s2))


def distance_i(s, t):

    # it will store the number of operation required to convert that string.
    dp = [[None for _ in range(len(s) + 1)] for __ in range(len(t) + 1)]

    # we instilize the boundry (if we have to convert _ to any string) case here.
    for idx in range(len(s) + 1):
        dp[0][idx] = idx

    for idx in range(len(t) + 1):
        dp[idx][0] = idx

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if t[row - 1] == s[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = (
                    min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]) + 1
                )

    return dp[-1][-1]


# geek --> geoeks
# remove, insert ya replace


if __name__ == "__main__":
    s1 = "geek"
    s2 = "geeks"
    distance_i(s1, s2)
