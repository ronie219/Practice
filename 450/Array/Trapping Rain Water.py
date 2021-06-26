# <-------------------------------TLE-------------------------------->
# N = 7
# array = [8, 8, 2, 4, 5, 5, 1]
#
# max_left = []
# max_right = []
# current_left_max = 0
# current_right_max = 0
# left = 0
# right = N - 1
# while left < N or right >= 0:
#     max_left.append(current_left_max)
#     max_right.insert(0, current_right_max)
#     if current_right_max < array[right]: current_right_max = array[right]
#     if current_left_max < array[left]: current_left_max = array[left]
#     left += 1
#     right -= 1
#
# # print(max_right)
# # print(max_left)
# max_storage = 0
# for n in range(1, N - 1):
#     if max_left[n] > array[n] and array[n] < max_right[n]:
#         max_storage += min(max_left[n], max_right[n]) - array[n]
# print(max_storage)

# <--------------------------------------------------------------------------------------------------------------->

N = 7
array = [8, 8, 2, 4, 5, 5, 1]
max_left = array[0]
max_right = array[N-1]
left = 0
right = N-1
current = max_left
total = 0
while left < right:
    if current > array[left]:
        total += current - array[left]
        left += 1
    else:
        current = array[left]
        if current > array[right]:
            total += current - array[right]
            right -= 1
print(total)
