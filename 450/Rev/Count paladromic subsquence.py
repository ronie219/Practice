def count_palamdromic_sub(arr):
    dp = [[None for _ in range(len(arr))] for __ in range(len(arr))]

    # we insilize the bounday case when i == j which mean we taking only one elememt like a, b, which is
    # palandrome
    for idx in range(len(arr)):
        dp[idx][idx] = 1

    for row in range(0, len(arr)):
        for col in range(0, row, -1):
            if arr[row] == arr[col]:
                dp[row][col] = dp[row][col-1] + dp[row+1][col] + 1
            else:
                dp[row][col] = dp[row][col-1] + \
                    dp[row+1][col] - dp[row-1][col-1]
    print(dp)


if __name__ == '__main__':
    string = 'abccbc'
    count_palamdromic_sub(string)
