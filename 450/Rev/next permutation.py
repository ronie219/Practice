def permutation(arr):

    peak_idx = None
    for idx in range(len(arr)-2, -1, -1):
        if arr[idx] < arr[idx+1]:
            peak_idx = idx
            break
    if peak_idx:
        jst_grt_number_idx = None
        diff = float('inf')
        for idx in range(len(arr)-1, peak_idx, -1):
            if arr[idx] - arr[peak_idx] < diff:
                diff = arr[idx] - arr[peak_idx]
                jst_grt_number_idx = idx
        arr[jst_grt_number_idx], arr[peak_idx] = arr[peak_idx], arr[jst_grt_number_idx]
        new_arr = arr[:jst_grt_number_idx] + arr[peak_idx::-1]
        return (new_arr)
    else:
        return arr[::-1]


print(permutation([1, 2, 3]))
