# def findLengthPalindrome(s,idx1,idx2):
#     count = 0
#     while idx1 >= 0 and idx2 < len(s):
#         if s[idx1] == s[idx2]:
#             count += 1
#             idx1 -= 1
#             idx2 += 1
#         else:
#             break
#     return count
#
#
# string = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
#
# total = 0
# for idx in range(0,len(string)):
#     palindrome_even = findLengthPalindrome(string, idx, idx)  # for even
#     palindrome_odd = findLengthPalindrome(string, idx, idx + 1)  # for odd
#     total += (palindrome_even + palindrome_odd)
#
# # print(total)
#
#
# string = "abccbc"
# lookup_matrix = []
#
# for row in range(len(string)):
#     arry = []
#     for col in range(len(string)):
#         if row == col:
#             arry.append(1)
#         elif string[row] == string[col]:
#             if len(string[row:col+1]) == 2:
#                 arry.append(3)
#             else:
#                 arry.append(lookup_matrix)
#         elif len(string[row:col+1]) == 2 and string[row] != string[col]:
#             arry.append(2)
#         else:
#             arry.append(None)
#     lookup_matrix.append(arry)
#
#
#
# for i in lookup_matrix:
#     print(i)

string = 'abcd'




def subsequence(sting,curr_idx,curr_str):
    if len(sting) == curr_idx :
        # result.append(curr_str)
        return [curr_str]
    result = []
    result.extend(subsequence(sting,curr_idx+1,curr_str+sting[curr_idx]))
    result.extend(subsequence(sting, curr_idx + 1, curr_str ))
    return result

# subsequence(string,0,'')
print(subsequence(string,0,''))