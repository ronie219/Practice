
# ATM
if __name__ == '__main__':
    def atm(amt, current_balance):
        return '%0.02f' %(current_balance - (
                int(amt) + 0.50)) if int(amt) % 5 == 0 and int(amt) >= 5 and (int(amt) + 0.50) < current_balance else "%0.02f" %current_balance


    a = list(map(float, input().split()))
    print(atm(a[0],a[1]))
