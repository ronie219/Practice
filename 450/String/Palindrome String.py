S = "abbaa"
start = 0
end = len(S) - 1
while start < end:
    if S[start] != S[end]:
        print(0)
        break
    start += 1
    end -= 1
else:
    print(1)