"""
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the length of longest bitonic subsequence of array.
Note - Bitonic subsequences begin with elements in increasing order, followed by elements in decreasing order.
"""


from collections import defaultdict


def bitnoic(arr):
    increasingDp = [0 for _ in range(len(arr))]
    increasingDp[0] = 1
    decreasingDp = [0 for _ in range(len(arr))]
    decreasingDp[-1] = 1
    dp = [0 for _ in range(len(arr))]

    for idx in range(1, len(arr)):
        max_count_sub = 0
        for bidx in range(idx-1, -1, -1):
            # we go backward and check that at what place we can attach the arr element

            if arr[idx] > arr[bidx] and increasingDp[bidx] > max_count_sub:
                max_count_sub = increasingDp[bidx]
        increasingDp[idx] = max_count_sub + 1

    for idx in range(len(arr)-2, -1, -1):
        max_count_sub = 0
        for bidx in range(idx+1, len(arr)):
            # we go backward and check that at what place we can attach the arr element

            if arr[idx] > arr[bidx] and decreasingDp[bidx] > max_count_sub:
                max_count_sub = decreasingDp[bidx]
        decreasingDp[idx] = max_count_sub + 1

    for idx in range(len(arr)):
        dp[idx] = increasingDp[idx] + decreasingDp[idx] - 1

    print(max(dp))


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 3]
    bitnoic(arr)
