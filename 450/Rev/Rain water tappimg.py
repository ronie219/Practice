def tappingWater(arr):

    # first we process the arr and try to find the max heighted building in my left
    # then we process the arr and try to find the max heighted building in my right
    cur_max = 0
    left = []
    for i in arr:
        cur_max = max(cur_max, i)
        left.append(cur_max)

    cur_max = 0
    right = []
    for i in arr[::-1]:
        cur_max = max(cur_max, i)
        right.append(cur_max)
    right.reverse()

    # now we check the min buliding at the current point which indicate the amount of water we can store
    unit_water = 0
    for i in range(len(arr)):
        unit_water += min(left[i], right[i]) - arr[i]
    print(unit_water)


if __name__ == '__main__':
    arr = [1, 1, 5, 2, 7, 6, 1, 4, 2, 3]
    tappingWater(arr)

0 + 0 + 1 + 2 + 1
