"""
1. You are given a string str.
2. You are required to calculate and print the count of subsequences of the nature a+b+c+.
For abbc -> there are 3 subsequences. abc, abc, abbc
For abcabc -> there are 7 subsequences. abc, abc, abbc, aabc, abcc, abc, abc.
"""


def subsquence(string):
    a_count = 0
    ab_count = 0
    abc_count = 0

    for s in string:
        if s == 'a':
            a_count = (a_count * 2) + 1
        elif s == 'b':
            ab_count = (ab_count * 2) + a_count
        elif s == 'c':
            abc_count = (abc_count * 2) + ab_count

    print(abc_count)


if __name__ == '__main__':
    string = 'abcabc'
    subsquence(string)
