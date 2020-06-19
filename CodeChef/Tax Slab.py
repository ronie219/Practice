# Tax Slabs
for _ in range(int(input())):
    N = int(input())
    tax = N
    tx_int = 0
    tax_per = [0.05, 0.10, 0.15, 0.20, 0.25]
    count = 0
    if N > 250000:
        tax -= 250000
        while tax > 0:
            if tax >= 250000 and count <= 4:
                tax -= 250000
                tx_int += 250000 * tax_per[count]
                count += 1
            elif count == 5 and tax > 0:
                tx_int += tax * 0.30
                break
            else:
                tx_int += tax * tax_per[count]
                break
    print(int(N - tx_int))
