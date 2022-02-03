"""
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are required to print the maximum profit you can make if you are allowed a single transaction.
"""


def profit(days, stock):
    maximum_profit = 0
    mini_cp = stock[0]

    for idx in range(days):
        if mini_cp > stock[idx]:
            mini_cp = stock[idx]
        if stock[idx] - mini_cp > maximum_profit:
            maximum_profit = stock[idx] - mini_cp

    print(maximum_profit)


if __name__ == '__main__':
    days = int(input('Enter days'))
    stock = list(map(int, input().split()))
    profit(days, stock)
