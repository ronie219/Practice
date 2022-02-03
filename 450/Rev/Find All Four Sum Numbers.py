def fourSum(arr, k):
    arr.sort()
    for p1 in range(0, len(arr)):
        for p2 in range(p1 + 1, len(arr)):
            si = p2+1
            ei = len(arr) - 1
            while si < ei:
                curr_sum = arr[p1] + arr[p2] + arr[si] + arr[ei]
                if curr_sum < k:
                    si += 1
                elif curr_sum > k:
                    ei -= 1
                else:
                    print((arr[p1], arr[p2], arr[si], arr[ei]))
                    si += 1
                    ei -= 1


arr = [0, 0, 2, 1, 1]
fourSum(arr, 3)
