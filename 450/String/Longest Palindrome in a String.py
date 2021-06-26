def longestPalin(S):
    max_palindrome = ''
    for idx in range(0, len(S)):
        palindrome_even = find_Palin(S, idx, idx)  # for even
        palindrome_odd = find_Palin(S, idx, idx + 1)  # for odd
        if len(palindrome_even) > len(max_palindrome): max_palindrome = palindrome_even
        if len(palindrome_odd) > len(max_palindrome): max_palindrome = palindrome_odd
    return max_palindrome


def find_Palin(s, idx1, ixd2):
    string_length = len(s)
    palindrome = ''
    while idx1 >= 0 and ixd2 < string_length:
        if s[idx1] != s[ixd2]:
            return palindrome
        else:
            palindrome = s[idx1:ixd2+1]
        ixd2 += 1
        idx1 -= 1
    return palindrome


S = "abc"
print(longestPalin(S))
