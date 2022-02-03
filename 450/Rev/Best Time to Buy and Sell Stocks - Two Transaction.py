

def Profit(arr):
    min_ptn = float('inf')
    max_pist = 0
    pist_arr = []

    for price in arr:
        min_ptn = min(min_ptn, price)
        max_pist = max(max_pist, price - min_ptn)
        pist_arr.append(max_pist)

    max_ptn = float('-inf')
    max_pibt = 0
    pibt_arr = []
    for price in arr[::-1]:

        max_ptn = max(max_ptn, price)
        max_pibt = max(max_pibt, max_ptn - price)
        pibt_arr.append(max_pibt)

    pibt_arr.reverse()

    max_profit = 0
    for idx in range(len(arr)):
        max_profit = max(max_profit, pist_arr[idx]+pibt_arr[idx])

    return max_profit


if __name__ == '__main__':
    arr = [30, 40, 43, 50, 45, 20, 26, 40, 80,
           50, 30, 15, 10, 20, 40, 45, 71, 50, 55]
    print(Profit(arr))
