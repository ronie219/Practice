import bisect
import math
import os
import random
import re
import sys
from collections import deque
def meidan(arr):
    arr = list(arr)
    m = len(arr)//2
    if len(arr) % 2 == 0:
        return sum(arr[m - 1:m + 1]) / 2
    else :
        return arr[int(m)]   
    
        
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    var = deque(sorted(expenditure[:d]))
    for i in range(d,len(expenditure)):
        if (meidan(var) * 2) <= expenditure[i]:
            print(meidan(var))
            print(var)
            print(expenditure[i])
            notifications += 1
        var.popleft()
        bisect.insort(var,expenditure[i])
    return (notifications)

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
