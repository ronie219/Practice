from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    output = []
    dfs(sorted(candidates), 0, target, [], output)
    return output


def dfs(arr, idx, total, current, output):
    for c_idx in range(idx, len(arr)):
        if total - arr[c_idx] <= 0:
            if total - arr[c_idx] == 0:
                output.append(current + [arr[c_idx]])
            return

        if c_idx > idx and arr[c_idx] == arr[c_idx-1]:
            continue

        dfs(arr, c_idx+1, total - arr[c_idx], current + [arr[c_idx]], output)


a = [10,1,2,7,6,1,5]
t = 8
print(combinationSum2(a,t))