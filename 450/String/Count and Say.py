def countAndSay(N):
    if N == 1:
        return "1"
    string = countAndSay(N - 1)
    count = 1
    current = string[0]
    start = 1
    output = ''
    while start < len(string):
        if string[start] == current:
            count += 1
            current = string[start]
        else:
            output += (str(count) + current)
            current = string[start]
            count = 1
        start += 1
    output += (str(count) + current)

    return output


print(countAndSay(5))

"111221"
