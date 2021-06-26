# New Year Chaos
for _ in range(int(input())):
    N = int(input())
    q = list(map(int,input().split()))
    swap = 0
    for i in range(len(q)-1,0,-1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                swap += 1
                q[i],q[i-1] = q[i-1], q[i]
            elif q[i - 2] == i+1:
                swap += 2
                q[i-2],q[i-1] = q[i-1], q[i-2]
                q[i],q[i-1] = q[i-1], q[i]
            else:
                print("Too chaotic")
                break
    else:
        print(swap)