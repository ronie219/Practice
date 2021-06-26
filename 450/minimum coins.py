
def coin_count(target, coins):

    if target <= 0:
        return 0
    arr = target + 1
    for i in range(len(coins)):
        if target - coins[i] >= 0:
            temp = coin_count(target - coins[i], coins)
            arr = min(arr, temp + 1)
    return arr


coins = [1, 7, 10]
target = 39
print(coin_count(target, coins))