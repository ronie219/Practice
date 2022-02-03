def merge(arr1, arr2):
    # insertion sort
    s1 = 0
    # s2 = 0
    while s1 < len(arr1):
        if arr1[s1] > arr2[0]:
            arr1[s1], arr2[0] = arr2[0], arr1[s1]
            idx = 0
            while idx < len(arr2):
                if arr2[idx] > arr2[idx + 1]:
                    arr2[idx], arr2[idx + 1] = arr2[idx + 1], arr2[idx]
                    idx += 1
                else:
                    break
            s1 += 1
        elif arr1[s1] >= arr2[0]:
            s1 += 1


if __name__ == '__main__':
    arr1 = [0, 1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    merge(arr1, arr2)
    print(arr1+arr2)
    # print(arr2)
