arr = [1,0, 5, 8 ,9 ,2, 6, 7, 6, 8, 9]

def find_min_jump(arr):
    if arr[0] == 0: print(-1)
    jump = 1
    step = arr[0]
    max_reach = arr[0]

    for num in range(1,len(arr)):
        #print(num,max_reach)
        if num > max_reach:
            return -1
        max_reach = max(max_reach,num+arr[num])

        step -= 1



        if step == 0:
            step = max_reach - num
            jump += 1
    return jump

print(find_min_jump(arr))

