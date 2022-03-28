"""
def maxTaxiEarnings(n, rides):
    rides.sort(key=lambda x: x[1])

    def _inner(n, ride, mx_idx):
        if n == 0:
            return 0
        opt1 = 0
        # option-1 we choose the first ride
        if mx_idx < ride[0][1]:
            opt1 = _inner(n - 1, ride[1:], rides[0][1]) + (ride[0][1] - ride[0][0] + ride[0][2])

        # option-2 we choose the first ride
        opt2 = _inner(n - 1, ride[1:], mx_idx)

        return max(opt1, opt2)

    return _inner(len(rides), rides, 0)
"""
def maxTaxiEarnings(n, rides):
    rides.sort(key=lambda c : c[1])
    dp_arr = [0 for _ in range(rides[-1][1] + 1)]

    dp_pt = 0
    rides_pt = 0
    while dp_pt < len(dp_arr):
        if rides_pt < len(rides) and rides[rides_pt][1] == dp_pt :
            while  rides_pt < len(rides) and rides[rides_pt][1] == dp_pt:
                cal = rides[rides_pt][1] - rides[rides_pt][0] + rides[rides_pt][2] + dp_arr[rides[rides_pt][0] - 1]
                dp_arr[dp_pt] = max(dp_arr[dp_pt],cal)
                rides_pt += 1
        else:
            dp_pt += 1
    print(dp_arr)





n = 5
rides = [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
print(maxTaxiEarnings(n, rides))


