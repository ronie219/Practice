"""
1. You are given a number n, representing the number of opening brackets ( and closing brackets )
2. You are required to find the number of ways in which you can arrange the brackets if the closing brackets should never exceed opening brackets
e.g.
for 1, answer is 1 - ()
for 2, answer is 2 - ()(), (())
for 3, asnwer is 5 - ()()(), () (()), (())(), (()()), ((()))
"""
# prerqusite id Cathalen Numbers


def parenthisCount(num):
    dp = [0 for _ in range(num+1)]
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
    num = int(input())
    parenthisCount(num)
