#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    toys = 0
    for i in range(len(prices)):
        item = []
        try:
            while (sum(item) + prices[i]) <= k and prices[i] <= k:
                item.append(prices[i])
                i += 1
        except IndexError:
            break
        if toys < len(item):
            toys = len(item)
    return toys


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
