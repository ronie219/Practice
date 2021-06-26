string1 = "ab12"
string2 = 'abb34'
shuffle_string ='abbab1234'
pointer_one = 0
pointer_two = 0

if len(string2) + len(string1) == len(shuffle_string):
    for i in shuffle_string:
        if pointer_one < len(string1) and string1[pointer_one] == i:
            pointer_one += 1
        elif pointer_two < len(string2) and string2[pointer_two] == i:
            pointer_two += 1
        else:
            print("NO")
            break
    else:
        print("Yes")
else:
    print("NO")