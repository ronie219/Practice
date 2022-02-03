"""
find all the binary strings of length with no consecutive zero's. In this problem,

1. You are given a number n.
2. You are required to print the number of binary strings of length n with no consecutive 0's.

"""

def printBinary(n):
 
    zeroCount = 1
    oneCount = 1

    for _ in range(1,n):
        temp = zeroCount
        zeroCount = oneCount
        oneCount = temp + oneCount
    
    print(zeroCount + oneCount)

if __name__ =='__main__':
    n = 6
    printBinary(n)