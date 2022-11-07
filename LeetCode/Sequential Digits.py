def sequentialDigits(low, high):
    a = []

    for i in range(1, 10):
        num = i
        next_digit = i + 1

        while num <= high and next_digit <= 9:
            num = num * 10 + next_digit
            if low <= num <= high:
                a.append(num)
            next_digit += 1

    a.sort()
    return a


print(sequentialDigits(100,1000))