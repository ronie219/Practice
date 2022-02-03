def permutation(string):
    string = list(string)
    ans = []

    def inner(string, curr=''):
        if len(string) == 0:
            ans.append(curr)
            return

        for i in range(len(string)):
            inner(string[0:i] + string[i+1:], curr=curr+string[i])

    inner(string)
    return sorted(ans)


if __name__ == '__main__':
    s = 'ABSG'
    print(permutation(s))
