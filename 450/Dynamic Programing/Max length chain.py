# recursion


def maxChainLen(Parr, n):
    def _solve(arr, prev, pointer):

        # base case
        if pointer == n:
            return 0

        # we have 2 cases here we can include the item and exclude the item.
        val = arr[pointer]
        option1 = 0
        option2 = 0
        if prev < val[0]:
            option1 = _solve(arr, val[1], pointer + 1) + 1
        option2 = _solve(arr, prev, pointer + 1)

        return max(option1, option2)

    return _solve(Parr, -1, 0)


def maxChainLen(Parr, n):
    dp = [-1 for _ in range(n)]
    dp[0] = 1
    Parr.sort(key=lambda x: x[0])
    print(Parr)

    for idx in range(1, n):
        for bidx in range(idx - 1, -1, -1):
            if Parr[bidx][1] < Parr[idx][0] and dp[idx] < dp[bidx]:
                dp[idx] = dp[bidx] + 1

    print(dp)


if __name__ == "__main__":
    # arr = [
    #     (778, 887),
    #     (794, 916),
    #     (336, 387),
    #     (493, 650),
    #     (363, 422),
    #     (28, 691),
    #     (60, 764),
    #     (541, 927),
    #     (173, 427),
    #     (212, 737),
    #     (369, 568),
    #     (430, 783),
    #     (531, 863),
    #     (68, 124),
    #     (136, 930),
    #     (23, 803),
    #     (59, 70),
    #     (168, 394),
    #     (12, 457),
    #     (43, 230),
    #     (374, 422),
    #     (785, 920),
    #     (199, 538),
    #     (316, 325),
    #     (371, 414),
    #     (92, 527),
    #     (957, 981),
    #     (863, 874),
    #     (171, 997),
    #     (282, 306),
    #     (85, 926),
    #     (328, 337),
    #     (506, 847),
    #     (314, 730),
    # ]
    arr = [(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)]
    print(maxChainLen(arr, len(arr)))
