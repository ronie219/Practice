def fact(number):
    # num == 2 -> 2
    # fact(n-1) * number
    if number == 2 or number == 1:
        return number
    a = fact(number - 1) * number
    return a


print(fact(1))