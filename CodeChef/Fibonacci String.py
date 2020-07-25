# # Fibonacci String
# from collections import Counter
# for _ in range(int(input())):
#     s = input()
#     counter = Counter(s)
#     if len(set(s)) < 3:
#         print("Not")
#         continue
#     result = 0
#     i = max(counter.values())
#     while i != 0:
#         if (i - 1 and i -2) in counter.values():
#             print("Dynamic")
#             break
#         else:
#             print("Not")
#         i -= 1
#
