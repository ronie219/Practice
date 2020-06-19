
# Studying Alphabet
def Alphabet(s,book):
    for i in book:
        if i not in s:
            return "No"
    return "Yes"


s = input()
for _ in range(int(input())):
    book = input()
    print(Alphabet(s,book))
