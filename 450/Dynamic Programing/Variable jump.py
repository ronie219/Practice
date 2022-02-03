"""
1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. You are given n numbers, where ith element's value represents - till how far from the step  you could jump to in a single move.  
4. You are required to print the number of different paths via which you can climb to the top.
"""


# tableization + itteratve (top to bottom)
def variable_jumps_i(jumps, stairs):
    dp = [None for _ in range(stairs + 1)]
    dp[-1] = 1
    pointer = stairs - 1
    while pointer >= 0:
        count = 0
        for idx in range(1, jumps[pointer] + 1):
            if pointer + idx < len(dp):
                count += dp[pointer + idx]
        dp[pointer] = count
        pointer -= 1
    print(dp)


# recursion + memoization
def variable_jumps_r(jumps, stairs, dp, start=0):
    # base case
    if start == stairs:
        return 1

    # memoize the result
    if dp[start]:
        return dp[start]

    # recurrsive intution
    count = 0
    print("idx + ", start)
    for idx in range(1, jumps[start] + 1):
        if start + idx <= stairs:
            count += variable_jumps_r(jumps, stairs, dp, start + idx)

    dp[start] = count
    return count


if __name__ == "__main__":
    stair_jump = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    stair = len(stair_jump)
    dp = [None for _ in range(stair)]
    variable_jumps_i(stair_jump, stair)
    print(variable_jumps_r(stair_jump, stair, dp))
    print(dp)
