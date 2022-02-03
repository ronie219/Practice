"""
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are required to print the maximum profit you can make if you are allowed infinite transactions.
Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) before opening another transaction (another buy)
"""


def InfiniteTransaction(arr, n):
    total_profit = 0
    spidx = 0
    cpidx = 0

    for idx in range(1, n):
        if arr[idx - 1] > arr[idx]:
            total_profit += arr[spidx] - arr[cpidx]
            spidx = cpidx = idx
        else:
            spidx += 1

    total_profit += arr[spidx] - arr[cpidx]
    print(total_profit)


def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    InfiniteTransaction(array, n)


if __name__ == '__main__':
    main()
