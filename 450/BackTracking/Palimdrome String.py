def partition(string,curr=[]):

    if string == "":
        print(curr)
        return 

    for end in range(len(string)):
        if isPalimdrome(string[0:end+ 1]):
            curr.append(string[0:end+ 1])
            partition(string[end+1:])
            curr.pop()
    
def isPalimdrome(string):
    start = 0
    end = len(string) - 1

    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    
    return True


if __name__ == '__main__':
    partition('nittin')