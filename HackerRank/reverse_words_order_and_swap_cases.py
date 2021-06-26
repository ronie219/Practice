
def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    sentence = sentence.split(" ")
    sentence.reverse()
    result = ''
    for i in sentence:
        strt = ''
        for j in i:
            if j.islower():
                strt += j.upper()
            else:
                strt += j.lower()
        result += (strt + ' ')
    return result[:-1]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
    # fptr.write(result + '\n')

    ## fptr.close()