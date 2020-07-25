# Sherlock and Anagrams
from collections import Counter


def sherlockAndAnagrams(s):
    d = Counter(s)
    i = 2
    while i < len(s):
        for j in range(len(s)):
            if j + i <= len(s):
                d[''.join(sorted(s[j:j + i]))] += 1
            else:
                break
        i += 1
    count = 0
    for i in d.items():
        count += i[1] * (i[1] - 1) // 2
    return count


q = int(input())
for q_itr in range(q):
    s = input()
    result = sherlockAndAnagrams(s)
