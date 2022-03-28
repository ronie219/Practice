def combinationSum(candidates, target):
    # candidates.sort()

    # dfs solution
    def inner(arr, answer, idx=0, pairs=[], till_sum=0):
        if idx == len(arr): return
        if till_sum == target:
            answer.append(pairs)
            return
        if till_sum > target: return

        # we have 2 options
        # take the char or reject that char

        inner(arr, answer, idx, pairs + [str(arr[idx])], till_sum + arr[idx])
        inner(arr, answer, idx + 1, pairs, till_sum)

    answer = []
    inner(candidates, answer)
    return answer


print(combinationSum([2, 2, 3, 6, 7], 7))
