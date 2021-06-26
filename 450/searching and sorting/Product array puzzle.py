def productExceptSelf(nums, n):
    total = 1
    for ele in nums:
        if ele != 0:total *= ele
    output = []
    for ele in nums:
        if ele == 0:
            output.append(total)
        else:
            output.append(total // ele)
    return output

print(productExceptSelf([1,0],5))