def permutation(string, step=0,out=[]):
    if step == len(string):
        out.append("".join(string))
    else:
        for i in range(step,len(string)):
            # string_copy = string
            string = [i for i in string]
            string[i],string[step] = string[step], string[i]
            (permutation("".join(string),step+1))
    return out


string = 'abc'
print(permutation(string))


