prices = [7, 1, 5, 3, 6, 4]
min_rate = max(prices)
profit = 0
for stock in prices:
    if stock <= min_rate:
        min_rate = stock
    else:
        if profit < stock - min_rate:
            profit = stock - min_rate

print(profit)
print(min_rate)
