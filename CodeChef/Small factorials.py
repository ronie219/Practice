# Small factorials
for _ in range(int(input())):
    fact = 1
    for i in range(1,int(input())+1):
        fact = fact * i
        i += 1
    print(fact)
