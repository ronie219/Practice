"""
1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. In one move, you are allowed to climb 1, 2 or 3 stairs.
"""

import time


# recuursion + memoization
def climbingStairs_r(stairs, steps, dp):
    # base case
    if stairs == 0:
        return 1

    # mem0ized answers if available it will return
    if dp[stairs] != 0: 
        return dp[stairs]

    # recuursive relation

    count = 0
    for step in steps:
        if stairs - step >= 0:
            count += climbingStairs_r(stairs - step, steps, dp)

    # string the calculated result
    dp[stairs] = count
    return count


# tableization + itterative (bottom to top)
def climbingStairs_i(stairs, steps):
    dp = [None for _ in range(stairs + 1)]
    dp[0] = 1
    for idx in range(1, len(dp)):
        count = 0
        for step in steps:
            if idx - step >= 0:
                count += dp[idx - step]
        dp[idx] = count
    print(dp)


if __name__ == '__main__':
    begin = time.time()
    steps = 10
    p_steps = [1, 2, 3]
    dp = [0 for _ in range(steps + 1)]
    print(climbingStairs_r(steps, p_steps, dp))
    print(f"Execution time : {time.time() - begin}")

    begin = time.time()
    climbingStairs_i(steps, p_steps)
    print(f"Execution time : {time.time() - begin}")
