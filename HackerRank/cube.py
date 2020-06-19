
d = input('Enter the Dimension of the cube').split()
n = input('Enter value N')
out = []
for i in range(0, int(d[0]) + 1):
    for j in range(0, int(d[1]) + 1):
        for k in range(0, int(d[2]) + 1):
            if i + j + k != n:
                out.append([i , j , k])
            else:
                pass
print(out)
