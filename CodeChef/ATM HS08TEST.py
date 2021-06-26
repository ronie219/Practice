try:
    x, y = map(float, (input().split()))

    if x + 0.5 <= y and int(x) % 5 == 0:
        print('%.2f' % ((y - x) - .5))
    else:
        print('%.2f' % y)

except:
    pass
