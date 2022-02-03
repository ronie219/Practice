"""
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the length of longest increasing subsequence of array.

such as 10 22 9 33 21 50 41 60 80 3 ---> 10 22 33 50 60 80
"""

# itterative + tablulization

from collections import defaultdict


def longest_subsquence_i(arr):

    # we create a dp of same size of arr present and assign meaning in each cell such as
    # in each cell we store the count of subsequence end with that number in the arr respectively
    dp = [0 for _ in range(len(arr))]
    dp[0] = 1
    paths = defaultdict(list)
    paths[1].append([str(arr[0])])

    for idx in range(1, len(arr)):
        max_count_sub = 0
        for bidx in range(idx-1, -1, -1):
            # we go backward and check that at what place we can attach the arr element

            if arr[idx] > arr[bidx] and dp[bidx] > max_count_sub:
                max_count_sub = dp[bidx]
        print(paths)
        for path in paths[max_count_sub]:

            paths[max_count_sub + 1].append(path + [arr[idx]])
        dp[idx] = max_count_sub + 1
    print(max(dp))
    print(paths[max(dp)])


# recursive + memoization
def longest_subsquence_r(arr):
    memo = {}

    def _solve(arr, curr=0, prev=-1):
        # base case
        if len(arr) == curr:
            return 0

        # recursive intuation

        # we have to two options 1. we can include that item 2. we can exclude that item.
        if (curr, prev) in memo:
            return memo[(curr, prev)]
        opt1 = 0
        # include
        if prev == -1 or arr[curr] > arr[prev]:
            opt1 = 1 + _solve(arr, curr+1, curr)

        # exclude
        opt2 = _solve(arr, curr + 1, prev)
        memo[(curr, prev)] = max(opt1, opt2)
        return max(opt1, opt2)
    print(_solve(arr))


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 3]
    longest_subsquence_i(arr)
    longest_subsquence_r(arr)
