# Chef and Recipe 
from collections import Counter
def recipe(indigredent):
    for i in range(len(indigredent)):
        bol = True
        for j in range(i, len(indigredent)):
            if indigredent[i] == indigredent[j] and bol is True:
                continue
            elif bol is False and indigredent[i] == indigredent[j]:
                return "NO"
            else:
                bol = False
    cnt = Counter(indigredent)
    lst_cnt = [i[1] for i in cnt.items()]
    if len(lst_cnt) != len(set(lst_cnt)):
        return "NO"
    return "YES"
for _ in range(int(input())):
    rec_num = int(input())
    rec = list(map(int, input().split()))
    print(recipe(rec))