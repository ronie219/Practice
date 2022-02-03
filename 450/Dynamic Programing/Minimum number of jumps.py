# recurrsioon
def minJumps(arr, n):
    meme = {}

    def _solve(arr, n, start):
        if start >= n - 1:
            return 0

        if start in meme.keys():
            return meme[start]

        mini_path = float("inf")

        for idx in range(1, arr[start] + 1):
            mini_path = min(mini_path, _solve(arr, n, start + idx))

        meme[start] = mini_path + 1
        return mini_path + 1

    return _solve(arr, n, 0)


if __name__ == "__main__":
    ar = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    n = 11
    print(minJumps(ar, n))
