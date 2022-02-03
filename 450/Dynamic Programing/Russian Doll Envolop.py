"""
1. You are given a number n, representing the number of envelopes.
2. You are given n pair of numbers, representing the width and height of each envelope.
3. You are required to print the count of maximum number of envelopes that can be nested inside each other.
Note - Rotation is not allowed.
"""

from collections import defaultdict


def russain_doll(arr, n):
    arr.sort(key=lambda x: x[0])
    print(arr)
    dp = defaultdict(int)

    for udoll in range(len(arr)):
        maxi_doll = 0
        for idoll in range(udoll):
            if arr[idoll][1] < arr[udoll][1] and dp[arr[idoll][0]] > maxi_doll:
                maxi_doll = dp[arr[idoll][0]]
        dp[arr[udoll][0]] = maxi_doll + 1

    print(dp)


if __name__ == '__main__':
    n = 10
    arr = [[17, 5], [26, 18], [25, 34], [48, 84], [63, 72], [
        42, 86], [9, 55], [4, 70], [21, 45], [68, 76], [58, 51]]
    russain_doll(arr, n)
