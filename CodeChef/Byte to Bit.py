
# Byte to Bit
for t in range(int(input())):
    N = int(input())
    Bits, Nibbles, Bytes = 1, 0, 0
    while N > 0:
        if Bits != 0:
            N -= 2
            if N > 0:
                Nibbles += Bits
                Bits = 0
        if Nibbles != 0:
            N -= 8
            if N > 0:
                Bytes += Nibbles
                Nibbles = 0
        if Bytes != 0:
            N -= 16
            if N > 0:
                Bits += 2 * Bytes
                Bytes = 0
    print(Bits, Nibbles, Bytes)