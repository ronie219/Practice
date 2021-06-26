N = 4
K = 2
arr = [1, 1, 1, 1]
# track = {}
# count = 0
# for i in arr:
#     if i in track:
#         count += 1
#     else:
#         track[K - i] = i
#
# print(count*2)
# print(track)
left = 0
right = N - 1
count = 0
arr.sort()
while left < right:
    if arr[left] + arr[right] > K:
        right -= 1
    elif arr[left] + arr[right] < K:
        left += 1
    else:
        count += 1
        right = -1
        left = +1
print(count)
