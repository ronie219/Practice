# l1 = [1, 2, 3, 5]
# l2 = [4, 6, 7, 8]
# len1 = len(l1)
# len2 = len(l2)
# l1 += l2
# l2 = None
# i = 0
# print(l1)
# while i < len(l1):
#     ind = i
#     for j in range(i + 1, len(l1)):
#         if l1[ind] > l1[j]:
#             ind = j
#     l1[i], l1[ind] = l1[ind], l1[i]
#     i += 1
# print(str(l1[:len1])+ '\n' + str(l1[len2:]))

# from pycountry import countries
# import geograpy
# # print(countries.get(name = 'India'))
# url = 'http://www.bbc.com/news/world-europe-26919928'
# a = geograpy.get_place_context(url=url)
# print(a.places)
#
# import ctypes
#
#
# class DynamicArry():
#
#     def __init__(self):
#         self.size = 1
#         self.n = 0
#         self.A = self.make_array(self.size)
#
#     def __len__(self):
#         return self.n
#
#     def __getitem__(self, index):
#         if not 0 < index < self.n:
#             return IndexError("Index out of bound")
#         return self.A[index]
#
#     def add(self, ele):
#         if self.n == self.size:
#             self._resize(2 * self.size)
#         self.A[self.n] = ele
#         self.n += 1
#
#     def _resize(self, new_size):
#         B = self.make_array(new_size)
#         for i in range(self.n):
#             B[i] = self.A[i]
#         self.A = B
#         self.size = new_size
#
#     def make_array(self, size):
#         return (ctypes.py_object * size)()
#
# arr = DynamicArry()
# arr.add(1)
# arr.add(2)
# arr.add(3)
# arr.add(4)
# arr.add(5)
# print(len(arr))
# print(arr.__getitem__(1))
#
#
# def large_count_sum(arr):
#     if len(arr) == 0:
#         return 0
#     total = 0
#     count = 0
#     for i in arr:
#         if 0 <= count:
#             count += i
#             if count > total:
#                 total = count
#         else:
#             count = 0
#     print(total)
#
#
# large_count_sum([1, 2, -1, 3, 4, 10, 10, -10])
