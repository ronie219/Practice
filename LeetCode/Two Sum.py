# Two Sum

def twoSum(nums,target):
    read ={}
    result= []
    for i in range(len(nums)):
        if nums[i] in read.keys():
            result += read[nums[i]],i
        else:
            read[target - nums[i]] = i
    return (result)
