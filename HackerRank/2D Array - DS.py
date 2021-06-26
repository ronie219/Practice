# 2D Array - DS
import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_value = -1000
    for i in range(1,5):
        for j in range(1,5):
            hourglass = arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            max_value = hourglass if hourglass > max_value else max_value
    return max_value


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglassSum(arr))
