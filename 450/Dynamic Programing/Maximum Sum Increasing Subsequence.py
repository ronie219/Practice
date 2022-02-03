"""
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the sum of elements of the increasing subsequence with maximum sum for the array.
"""


def max_sum(arr):

    dp = [0 for _ in range(len(arr))]
    dp[0] = arr[0]

    for idx in range(1, len(arr)):
        max_sum = 0
        for bidx in range(idx-1, -1, -1):
            if arr[idx] > arr[bidx] and max_sum < dp[bidx]:
                max_sum = dp[bidx]
        dp[idx] = max_sum + arr[idx]
    print(dp)


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 3]
    max_sum(arr)
