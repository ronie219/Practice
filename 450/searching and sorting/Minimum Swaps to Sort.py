# using swap the element with position

def minSwaps(nums):
    scrap = []
    for ele in range(len(nums)):
        scrap.append((nums[ele], ele))
    scrap.sort(key=lambda x: x[0])
    swap = 0
    pointer = 0
    while pointer < len(scrap):
        if pointer != scrap[pointer][1]:
            temp = scrap[pointer]
            scrap[pointer] = scrap[scrap[pointer][1]]
            scrap[temp[1]] = temp
            swap += 1
        else:
            pointer += 1
    print(swap)

# using cycle method

def minimumSwap(num):
    scrap = sorted(num)
    dp = {}
    track = [False] * len(num)
    for ele,ele2 in zip(scrap,num):
        dp[ele] = ele2
    for idx in range(len(num)):
        if not track[idx]:
            track[idx] = True
            if scrap[idx] != num[idx]:
                pass



nums = [2, 8, 5, 4]
minimumSwap(nums)
