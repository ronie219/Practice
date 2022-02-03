def nCr(n,r):
    if n <= r : return 0
    memoization = {}
    def _fact(number):
        if number <= 1: return number
        if number in memoization: return memoization[number]
        return number * _fact(number-1)
    
    return (_fact(n)//(_fact(r)*_fact(n-r)))

if __name__ == '__main__':
    print(nCr(3,2))