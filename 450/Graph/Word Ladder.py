from collections import deque

class Solution:
    
    def _cobinations(self, word, wordlist,queue):
        wordList = set(wordlist)
        size = len(word)
        
        for i in range(size):
            word_arr = " ".join(word).split()
            for alphabets in range(97,123):
                word_arr[i] = chr(alphabets)
                if "".join(word_arr) in wordList:
                    wordList.remove("".join(word_arr))
                    queue.append("".join(word_arr))
        
        

    def ladderLength(self, beginWord, endWord, wordList):
        if len(endWord) != len(beginWord) : return 0
        if endWord == beginWord: return 1
        wordList = set(wordList)
        if endWord not in wordList: return 0
        wordList.add(beginWord)
        queue = deque()
        queue.append(beginWord)
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:return level
                for i in range(len(word)):
                    word_arr = " ".join(word).split()
                    for alphabets in range(97,123):
                        word_arr[i] = chr(alphabets)
                        if "".join(word_arr) == endWord:return level + 1
                        if "".join(word_arr) in wordList:
                            wordList.remove("".join(word_arr))
                            queue.append("".join(word_arr))
        return 0

                

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(s.ladderLength(beginWord,endWord,wordList))