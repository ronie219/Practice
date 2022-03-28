"""
For the recursive approach, we take the str1 and str1, and compare each char by char if char is equal that means we
can add those in our answer if they are not equal, then we discard that char from str1 and take the full str2 and vice
versa for the second str2 once.
"""

a = 'bl'
b = 'yby'


def longestCommonSubsequence(string1: str, string2: str) -> str:
    memo = {}

    def inner(_str1, _str2, answer=''):
        if not _str1 or not _str2:
            return answer
        if (_str1, _str2) in memo.keys(): return memo[(_str1, _str2)]
        if _str1[0] == _str2[0]:
            answer += _str1[0]
            memo[(_str1, _str2)] = inner(_str1[1:], _str2[1:], answer)
            return memo[(_str1, _str2)]
        else:
            first = inner(_str1[1:], _str2, answer)
            second = inner(_str1, _str2[1:], answer)
            if len(first) > len(second):
                memo[(_str1, _str2)] = first
                return first
            memo[(_str1, _str2)] = second
            return second

    return inner(string1, string2)


print(longestCommonSubsequence(a, b))

"""
while using the top to down approach we are checking the conditions with both the string suing 2d matrix
 _ a b c d
_
a
b
c
f
e
in each cell we are storing the common sequence if the char are equal we are discard both the char and add 1 to it
if the char are not equal we will discard the char from str1 and char from str2 and take the max of it.
"""


def longestCommonSubsequence(string1: str, string2: str) -> str:
    dp = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string2))]

