"""
You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. You are given n numbers, where ith element's value represents - till how far from the step you could jump to in a single move.  You can of course jump fewer number of steps in the move.
4. You are required to print the number of minimum moves in which you can reach the top of staircase.
Note - If there is no path through the staircase print null.
"""


# recursion + memoization
def minimum_jump_r(jumps, stairs, dp, step=0):

    # base case
    if stairs - 1 == step:
        return 1

    # memoization
    if dp[step]:
        return dp[step]

    # recursive intiution
    path_count = [float('inf')]
    for idx in range(1, jumps[step]+1):
        if step + idx < stairs:
            path_count.append(minimum_jump_r(
                jumps, stairs, dp, step + idx) + 1)
    dp[step] = min(path_count)
    return dp[step]


def minimum_jumps_i(jumps, stairs):

    dp = [float('inf') for _ in range(stairs + 1)]
    dp[-1] = 0

    pointer = stairs - 1
    while pointer >= 0:
        mini = [float('inf')]
        for idx in range(1, jumps[pointer] + 1):
            if pointer + idx < len(dp):
                mini.append(dp[pointer + idx])
        dp[pointer] = min(mini) + 1
        pointer -= 1
    print(dp)


if __name__ == '__main__':
    stair_jumps = [3, 2, 4, 2, 0, 2, 3, 1, 2, 2]
    stairs = 10
    dp = [None for _ in range(stairs)]

    print(minimum_jump_r(stair_jumps, stairs, dp))
    print(dp)
    minimum_jumps_i(stair_jumps, stairs)
