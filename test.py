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

from pycountry import countries
import geograpy
# print(countries.get(name = 'India'))
url = 'http://www.bbc.com/news/world-europe-26919928'
a = geograpy.get_place_context(url=url)
print(a.places)