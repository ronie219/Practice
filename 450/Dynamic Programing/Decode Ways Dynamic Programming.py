"""
1. You are given a string str of digits. (will never start with a 0)
2. You are required to encode the str as per following rules
    1 -> a
    2 -> b
    3 -> c
    ..
    25 -> y
    26 -> z
3. You are required to calculate and print the count of encodings for the string str.

     For 123 -> there are 3 encodings. abc, aw, lc
     For 993 -> there is 1 encoding. iic 
     For 013 -> This is an invalid input. A string starting with 0 will not be passed.
     For 103 -> there is 1 encoding. jc
     For 303 -> there are 0 encodings. But such a string maybe passed. In this case 
     print 0.
"""


def encoding(string):
    if len(string) == 1:
        return 1
    if string[-1] == '0' and string[-2] == '0':
        return 0
    if int(string[-2] + string[-1]) > 26 and string[-1] == '0':
        return 0

    # we create a DP for the string the no. of encoding possible at that idx
    dp = [0 for _ in range(len(string) + 1)]
    dp[0] = 1
    dp[1] = 1

    for idx in range(2, len(dp)):
        count = 0
        if string[idx-1] == '0':
            count += dp[idx - 2]
        elif string[idx - 2] == '0':
            count += dp[idx - 1]
        else:
            count += dp[idx - 1]
            if int(string[idx-2] + string[idx - 1]) <= 26:
                count += dp[idx-2]
        dp[idx] = count
    # print(dp)
    return dp[-1]


if __name__ == '__main__':
    s = input().rstrip()
    print(encoding(s))
