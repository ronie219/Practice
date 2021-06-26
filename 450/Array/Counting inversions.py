n = [2, 4, 1, 3, 5]


def find_inversion(left_arr, right_arr, inversion=0):
    left = 0
    right = 0
    while len(left_arr) > left and len(right_arr) > right:
        if left_arr[left] > right_arr[right]:
            inversion += len(left_arr) - left - 1
            left += 1
        elif right_arr[right] > left_arr[left]:
            left += 1
            right = 0
    final = left_arr + right_arr
    print(inversion)
    return final.sort, inversion


def merge_sort(arr, lower, higher,inversion=0):
    if lower <= higher:
        mid = (higher - lower) // 2
        left_arr,inversion1 = merge_sort(arr[0:mid], 0, mid)
        right_arr,inversion2 = merge_sort(arr[mid:], mid, higher)
        final,inversion = find_inversion(left_arr, right_arr, (inversion1+inversion2))
        return final,inversion
    else:
        return arr,inversion


print(merge_sort(n, 0, len(n)))
