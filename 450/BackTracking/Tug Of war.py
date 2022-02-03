MIN_DIFF = float('inf')
ans = ()

def _towSolve(arr,idx,set1,set2,sum1,sum2):
    global MIN_DIFF
    global ans
    # base case here
    if idx == len(arr) and set1 and set2:
        if abs(sum1 - sum2) < MIN_DIFF:
            MIN_DIFF = abs(sum1 - sum2)
            ans = (set1, set2)
            print(ans)
            print(MIN_DIFF)
            print('*' * 20)
            return

    # opertion of set 1
    if len(set1) < (len(arr) + 1) // 2:
        set1.append(arr[idx])
        _towSolve(arr,idx+1,set1,set2, sum1+arr[idx], sum2)
        set1.pop()
    

    # opertion of set 2
    if len(set2) < (len(arr) + 1) // 2:
        set2.append(arr[idx])
        _towSolve(arr,idx+1,set1,set2, sum1, sum2+arr[idx])
        set2.pop()
        

def ToW(arr):
    set1 = []
    set2 = []
    _towSolve(arr, 0,set1, set2, 0, 0)


if __name__ == '__main__':
    ToW([1,2,3,4])
    print(ans)
    print(MIN_DIFF)