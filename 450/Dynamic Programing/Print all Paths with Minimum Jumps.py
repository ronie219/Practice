def path(arr):
    dp = [0 for _ in range(len(arr))]
    dp[-1] = 0

    # we find all the minimum possible path from that point

    for idx in range(len(arr) - 2, -1, -1):
        path = [float("inf")]
        for jump in range(idx + 1, idx + arr[idx]):
            path.append(dp[jump])
        dp[idx] = min(path)

    print(dp)


if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    path(arr)
