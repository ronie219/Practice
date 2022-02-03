"""

def rodCutting(arr):
    
    # cutting startegy
    new_arr = [None]
    new_arr.extend(arr)
    arr = new_arr
    del new_arr
    piece = {0:'',1:'1'}

    # arr used for reffering the previous record, it will keep record the best price till the length
    dp = [None for _ in range(len(arr))]
    dp[0] = 0
    dp[1] = arr[1]

    # we used for loop to fill the DP array and find best or max profit till that size.

    for idx in range(2, len(arr)):
        best_price = 0
        best_piece = ''
        for dpidx in range(1,idx+1):
            var = dp[idx - dpidx] + arr[dpidx]
            if best_price <= var:
                best_price = var
                best_piece = piece[idx - dpidx] + str(dpidx)
        dp[idx] = best_price
        piece[idx] = best_piece
    # print(dp)
    # print(piece[8])
    return dp[-1]

"""

def rodCutting(arr):

    # left - right startegy
    new_arr = [None]
    new_arr.extend(arr)
    arr = new_arr
    del new_arr
    piece = {0:'',1:'1'}

    # arr used for reffering the previous record, it will keep record the best price till the length
    dp = [None for _ in range(len(arr))]
    dp[0] = 0
    dp[1] = arr[1]

    # in left-right startegy if we divide the rod in x cut then we take cross of best solution of x and x-k for half cycle.

    for idx in range(2,len(arr)):
        best_price = arr[idx]
        best_peice = str(idx)
        count = idx // 2
        end = idx - 1
        start = 1
        print('*'*15)
        print(idx)
        while count != 0:
            print(start, end)
            var = dp[start] + dp[end]
            if best_price <= var:
                best_price = var
                best_peice = piece[start] + piece[end]
            start += 1
            end -= 1
            count -= 1
        dp[idx] = best_price
        piece[idx] = best_peice
    
    print(dp)
    print(piece)
    return (dp[-1])

if __name__ == '__main__':
    arr = [1,5,8,9,10,17,17,20]
    print(rodCutting(arr))