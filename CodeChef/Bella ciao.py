for _ in range(int(input())):
    D, d, P, Q = map(int, input().split())
    loop_count = D // d
    extra_days = D % d
    money = 0
    for day in range(loop_count):
        money += (P + (Q * day)) * d
    money += (P + (Q * (day+1))) * extra_days
    print(money)
