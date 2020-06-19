
# The Promised Land (Wrong)
output = []
for _ in range(int(input())):
    n, m = list(map(int, input().split()))  # super plot
    x, y, s = map(int, input().split())
    xi, yi, count, counts = ([0], [0], 0, 0)
    if x:
        for i in map(int, input().split()):
            xi.append(int(i))
    if y:
        for i in map(int, input().split()):
            yi.append(int(i))
    # print(xi)
    # print(yi)
    vertical = list()
    horizontal = list()
    count = 0
    for i in range(1, m + 1):
        if i in yi:
            horizontal.append(count)
            count = 0
        else:
            count += 1
    horizontal.append(count)
    for i in range(1, n + 1):
        if i in xi:
            vertical.append(count)
            count = 0
        else:
            count += 1
    vertical.append(count)
    count = 0
    for i in vertical:
        for j in horizontal:
            if i // s >= 1 and j // s >= 1:
                count += max(i // s, j // s)
    output.append(count)
for i in output:
    print(i)
    
# The Promised Land Right
c= []
for i in range(int(input())):
    n,m = map(int,input().split())
    x,y,s = map(int,input().split())
    xi,yi,count,counts = ([0],[0],0,0)
    if x:
        for i in map(int,input().split()):
            xi.append(int(i))
    if y:
        for i in map(int,input().split()):
            yi.append(int(i))
    xi.append(n+1)
    yi.append(m+1)
    for i in range(0,len(xi)-1):
        count += (xi[i+1]-xi[i]-1)//s
    for i in range(0,len(yi)-1):
        counts += (yi[i+1]-yi[i]-1)//s
    c.append(count*counts)
for i in c:
    print(i)
