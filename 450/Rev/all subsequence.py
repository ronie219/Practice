def subsequence(string):

    def inner(string, idx=0, curr=''):
        if idx == len(string):
            print(curr)
            return
        # taking the current char
        inner(string, idx + 1, curr+string[idx])
        # leaving the current char
        inner(string, idx + 1, curr)

    inner(string)


if __name__ == '__main__':
    s = 'aaa'
    subsequence(s)
