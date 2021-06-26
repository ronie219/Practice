"""Merge the Tools!"""

import textwrap


def merge_the_tools(string, k):
    l = textwrap.wrap(string, k)
    for i in range(len(string) // k):
        ls = list(dict.fromkeys(l[i]))
        print("".join(ls))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
