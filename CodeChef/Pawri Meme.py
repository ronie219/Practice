for _ in range(int(input())):
    s = input()
    new_string = ''
    i = 0
    while i <= len(s):
        try:
            if s[i] == 'p' and s[i:i+5] == "party":
                new_string += "pawri"
                i += 5
            #party
            else:
                new_string += (s[i])
                i += 1
        except:
            new_string += s[i:]
            break
    print(new_string)

    # yemaihuyemericarhaiauryahapartihorahihai
    # yemaihuyemericarhaiauryahapawrihorahihai