# Chef and Stringx
def lef_shif(s):
    return s[1:] + s[0]


def right_shift(s):
    return s[-1] + s[:-1]


for _ in range(int(input())):
    s = input()
    if lef_shif(s) == right_shift(s):
        print("YES")
    else:
        print("NO")