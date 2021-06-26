#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    swap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                swap += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print(f'Array is sorted in {swap} swaps'.format(swap=swap))
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
