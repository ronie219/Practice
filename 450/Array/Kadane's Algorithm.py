# N = 5
# arr = [1,2,3,-2,5]
# current_sum = 0
# max_sum = 0
# for i in arr:
#     current_sum += i
#     if current_sum > max_sum:
#         max_sum = current_sum
#     if current_sum < 0:
#         current_sum = 0
#
# print(max_sum)


N = 5
arr = [1,2,3,-2,5]

current = 0
max_sum = 0
for i in arr:
    current += i
    if max_sum < current:
        max_sum = current
    if current < 0:
        current = 0
print(max_sum)









