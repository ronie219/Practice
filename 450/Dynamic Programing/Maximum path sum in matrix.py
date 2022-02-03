# User function Template for python3


class Solution:
    def maximumPath(self, N, Matrix):
        dp = [[0 for _ in range(N)] for __ in range(N)]
        for row in range(N - 1, -1, -1):
            for col in range(0, N):
                if row == N - 1:
                    dp[row][col] = Matrix[row][col]
                else:
                    lside = 0
                    rside = 0
                    if col + 1 < N:
                        lside = dp[row + 1][col + 1]
                    if col - 1 >= 0:
                        rside = dp[row + 1][col - 1]
                    side = dp[row + 1][col]
                    dp[row][col] = Matrix[row][col] + max(lside, rside, side)
        for i in dp:
            print(i)
        return max(dp[0])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        Matrix = [[0] * N for i in range(N)]
        for itr in range(N * N):
            Matrix[(itr // N)][itr % N] = int(arr[itr])

        ob = Solution()
        print(ob.maximumPath(N, Matrix))
