def longest_increasing_subsequence(arr) -> int:
    import copy
    memo_cache = [copy.deepcopy([-1 for _ in range(len(arr))]) for __ in range(len(arr))]

    def inner(prev, idx, size=''):
        # base case
        if len(arr) == idx: return 0
        if memo_cache[prev][idx] != -1: return memo_cache[prev][idx]

        # we can ignore the idx
        size = inner(prev, idx + 1, size)

        # either we can take the idx
        if prev == -1 or arr[prev] < arr[idx]:
            size = max(size, (inner(idx, idx + 1, size) + 1))

        memo_cache[prev][idx] = size
        return size

    return inner(-1, 0)


print(longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))

