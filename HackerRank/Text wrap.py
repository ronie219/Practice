import textwrap

def wrap(string, max_width):
    val = (textwrap.TextWrapper(width=max_width).wrap(text=string))
    result = ''
    for i in val:
        result+= ((i) + '\n')
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)