"""
1. You are given a number n, representing the number of bridges on a river.
2. You are given n pair of numbers, representing the north bank and south bank co-ordinates of each bridge.
3. You are required to print the count of maximum number of non-overlapping bridges.
"""
from collections import defaultdict

def bridges(arr, n):
    # we will sort the arr on the basis of north bank and after that we will take LIS on the basis of south bank

    arr.sort(key=lambda x: x[0])

    # it will track all the max non overlapping bridges.
    dp = defaultdict(int)

    for north in range(len(arr)):
        maxi_bridge = 0
        for lis in range(north):
            if arr[lis][1] < arr[north][1] and dp[arr[lis][0]] > maxi_bridge:
                maxi_bridge = dp[arr[lis][0]]
        dp[arr[north][0]] = maxi_bridge + 1

    print(dp)


if __name__ == '__main__':
    n = 10
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    bridges(arr, n)
