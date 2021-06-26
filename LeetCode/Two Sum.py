# Two Sum

def twoSum(nums,target):
    read ={}
    result= []
    for i in range(len(nums)):
        if nums[i] in read.keys():
            result += read[nums[i]],i
        else:
            read[target - nums[i]] = i
    print(result)
    print(read)
    return (result)


twoSum([1,5,7,1],6)
twoSum([2,4,3,2],4)