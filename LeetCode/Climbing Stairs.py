class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1] * (n + 1)

        def rec(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if arr[n] == -1:
                arr[n] = rec(n - 1) + rec(n - 2)
            return arr[n]

        return rec(n)


def climbStairs(n):
    arr = [0, 1, 2]
    for i in range(3, n+1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr


print(climbStairs(6))
