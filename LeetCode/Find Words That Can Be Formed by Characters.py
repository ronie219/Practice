from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        bank = Counter(chars)
        print("bank:-->", bank)
        for word in words:
            print("word:-->", Counter(word))
            if Counter(word) <= bank:
                ans += len(word)
        return ans



