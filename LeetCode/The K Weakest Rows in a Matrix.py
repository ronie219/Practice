from typing import List


def binary_search(arr: List):
    if arr[0] == 0 : return 0
    start = 0
    end = len(arr) - 1
    right_most = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == 1:
            start = mid + 1
            right_most = mid
        else:
            end = mid - 1
    return right_most + 1


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    result = []
    for idx in range(len(mat)):
        len_of_army = binary_search(mat[idx])
        result.append([len_of_army, idx])
    print(result)
    result.sort(key=lambda x: x[0])
    result = [y for x, y in result]

    return result[:k]


print(kWeakestRows([[1, 0], [0, 0], [1, 0]], 2))
