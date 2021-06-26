# print multiplication --=-result
# print addtion -- result
# print Substrction -- result
# print Addtion Deco Funtion Completer
# print Multiplication

def addtion(func):
    def inner(a,b):
        print("Addtion", a + b)
        func(a,b)
        print("Addtion Completed")
    return inner

def multiplication(func):
    def inner(a,b):
        print("Multipication", a * b)
        func(a,b)
        print("Multiplication Completed")
    return inner


@multiplication
@addtion
def substract(a , b):
    print( a - b)

substract(50,10)


