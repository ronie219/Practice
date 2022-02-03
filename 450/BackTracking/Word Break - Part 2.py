def wordBreak(s, dic, sentense = ''):
    if s == '':
        print(sentense)
        return
    start = 0
    end = 1
    while end <= len(s):
        if s[start:end] in dic:
            wordBreak(s[end:], dic, sentense + s[start:end] + ' ')
        end += 1

if __name__ == "__main__":
    s = "catsanddog"
    n = 5
    dic = {"cats", "cat", "and", "sand", "dog"}
    wordBreak(s, dic)