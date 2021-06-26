def LongestRepeatingSubsequence(string):
    longest_string = string[0]
    current_string = ''
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if len(longest_string) < len(current_string): longest_string = current_string
        else:
            current_string += string[i]

    return len(longest_string)


print(LongestRepeatingSubsequence('agcsorvauz'))
