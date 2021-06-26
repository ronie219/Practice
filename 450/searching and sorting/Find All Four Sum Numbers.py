arr = [2,2,2,2,2]
k = 8
output = []
arr.sort()
for i in range(len(arr)):
    for j in range(i+1,len(arr)-1):
        left = j + 1
        right = len(arr) - 1
        target_sum = k - (arr[i] + arr[j])
        while left < right:
            if arr[left] + arr[right] == target_sum:
                result = [arr[i],arr[j],arr[left],arr[right]]
                if result not in output:output.append(result)
                right -= 1
                left += 1
            elif arr[left] + arr[right] < target_sum:
                left += 1
            else:
                right -= 1
print(output)