
# Safe Robots
for _ in range(int(input())):   #wrong
    s = input()
    A, B = map(int, input().split())
    Bs = 0
    As = 0
    if s.index("A") > s.index("B"):
        print("Safe")
    elif s.index("A") == s.index("B"):
        print("Unsafe")
    else:
        while Bs != -len(s) or As != len(s):
            if (As + 1) == len(s)+Bs:
                print("Unsafe")
                break
            else:
                Bs -= B
                As += A
        else:
            print("Safe")

for _ in range(int(input())):   #Right 
    s = input()
    A, B = map(int, input().split())
    distance = abs(s.index("A") - s.index("B"))
    if distance % (A + B) == 0:
        print("unsafe")
    else:
        print("safe")