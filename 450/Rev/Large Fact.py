def factorial(number):

    carry = 0
    fact = [1]

    for num in range(2, number + 1):

        for j in range(len(fact)):
            var = num * fact[j] + carry
            fact[j] = var % 10
            carry = var // 10

        while carry != 0:
            fact.append(carry % 10)
            carry = carry // 10

    return fact[::-1]


print(factorial(10))
