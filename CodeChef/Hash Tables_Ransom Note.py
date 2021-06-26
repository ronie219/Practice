# Hash Tables: Ransom Note
from collections import Counter
def checkMagazine(magazine, note):
    n = Counter(note)
    m = Counter(magazine)
    for i in n:
        if i in m.keys() and n.get(i) <= m.get(i):
            continue
        else:
            print("No")
            break
    else:
        print("Yes")


mn = input().split()
m = int(mn[0])
n = int(mn[1])
magazine = input().rstrip().split()
note = input().rstrip().split()
checkMagazine(magazine, note)
