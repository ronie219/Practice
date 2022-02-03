# def subsequence(output,idx, string):
#     if len(string) == idx:
#         print(output)
#     else:
#         subsequence(output,idx+1,string)
#         output += string[idx]
#         subsequence(output,idx+1,string)
#

def power_set(string, idx=0, current=''):
    if idx == len(string):
        print(current)
    else:
        power_set(string, idx+1, current)
        current += string[idx]
        power_set(string, idx+1, current)


string = ['a', 'b', 'c']
string = 'abc'
# subsequence("",0,string)
power_set(string)
