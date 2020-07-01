# Counting Valleys
def countingValleys(n, s):
    count = 0
    down = False
    valley = 0
    for i in range(n):
        if s[i] == 'U':
            count += 1
        else:
            count -= 1
        if count < 0 and down is False:
            valley += 1
            down = True
        elif count >= 0:
            down = False
    return valley


n = int(input())
s = input()
print(countingValleys(n, s))
