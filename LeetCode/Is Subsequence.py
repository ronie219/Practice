# def isSubsequence(self, s: str, t: str) -> bool:
#     sub = 0
#     main = 0
#     while sub < len(s) and main < len(t):
#         if s[sub] == t[main]:
#             sub += 1
#             main += 1
#         else:
#             main += 1
#     return True if sub == len(s) else False

# def isSubsequence(s, t):
#     t = iter(t)
#     print(t)
#     print([c in t for c in s])
#     return all(c in t for c in s)

# print(isSubsequence("abc", "cabdabc"))

# List, Tuple and set
#
# var_list = [10, 20, 30, "Abhishek", 25, 1995]
# var_list2 = [11, 21, 31, "Rohit", 24, 1996]
#
# print(var_list[2])  # Positive Indexing
#
# print(var_list[-5])  # negative indexing
#
# var_list[3] = ["Biswas"]  # Mutable and support and type of data type
# var_list2[3] = "Singh"
#
# # print(var_list)
# # print(var_list2)
#
# # for i in var_list2: # it a type of iterator
# # print(i)
#
# # operation
#
# var_list.append("New thing")
# print(var_list.count(20))
# # print(var_list.pop())
# var_list.remove("New thing")
# # var_list.extend(var_list2)
# # var_list2.sort() # having same data type
# # a = ["abhishek","biswas","aaksdk"]
# # a.sort()
# # var_list.insert(0,"New")
# print(var_list.index(25))
# # var_list.clear()
# a = var_list.copy()
# print(var_list[0:2])
#
#
#
# # ************************ Tuple *************************
#
# var_list = (10, 20, 30, "Abhishek", 25, 1995,20)
# for i in var_list:
#     print(i)
#
# # *************************** Set ***********************
# a = {8, 2, 3,4,5,5,"Abhoshek","Biswas",-1}
# print(a)
# print(a)

amount = input()
amount = int(amount)
print(type(amount))
tip_percent = 10  # 10 percent ka tip lunga
print(amount * (tip_percent / 100))


def func():
    return 1, 2, 3


print(type(func()))
