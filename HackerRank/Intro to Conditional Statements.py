
if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1:
        print("Weird")
    else:
        if N in range(2,5):
            print("Not Weird")
        elif N in range(6, 20):
            print("Weird")
        else:
            print("Not Weird")