def print_rangoli(size):
    char = list(map(chr,range(97,(97+size))))
    back = '-'.join(char[1:])
    front = '-'.join(char[::-1])
    string = front+ '-' + back
    width = len(string)
    length = (width//2)+1
    n = 0
    for i in range((size*2)- 1):
        print(back[-i]+front[i].center(width,'-'))
        n += 2



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)