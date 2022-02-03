"""
1. You are given a number n, representing the number of elements.
2. You are required to find the number of Binary Search Trees you can create using the elements.
"""

# iterative + tableization


def bstCount_i(num):

    # we create a dp in which we store the count of bst we can create with numbers of node.
    dp = [0 for _ in range(num + 1)]
    dp[0] = 1
    dp[1] = 1

    for idx in range(2, len(dp)):
        left = 0
        right = idx-1
        bst_count = 0
        while left < idx and right >= 0:
            bst_count += dp[left]*dp[right]
            left += 1
            right -= 1
        dp[idx] = bst_count
    print(dp[-1])


if __name__ == '__main__':
    n = int(input())
    bstCount_i(n)
