'''
# Factorial
a = 1
b = int(input('Enter a Number: '))
for i in range(b,1,-1):
    a = a * i
print(a)
'''\
#
'''
# Armstrong Number 
a = input('Enter a Number : ')
b = 0
for i in range(len(a)):
    b = pow(int(a[i]),len(a)) + b
print(b)
if(int(a) == b):
    print('Armstrong number')
else:
    print('Not Armstrong number')
'''\
'''
# Prime Number in range
start = int(input('Enter a Start Range : '))
end = int(input('Enter a End Range : '))
for i in range(start,end,1):
    for a in range(2,i + 1,1):
        if i == a:
            print(i)
        if (i % a) == 0:
            break
        else:
            continue
'''\
'''
# Fibonacci=
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(3))
'''\
'''
a = input('Enter a list seperated by , ')
a = a.split(',')
(a[0],a[-1])  = a[-1],a[0]
print(a)
'''\
'''

# Reversing
a = [1 , 2 , 3, 4 ]
b = []
#print(a.clear())
for i in range(len(a),0,-1):
    b.append(i)
print(b)
'''\
'''
# N  Number of largest Number
a = [50,4,53,555,21,60,11.2,10]
a.sort()
print(a)
# print(min(a))
b = int(input('Enter Number of largest Number '))
for i in range(-1,-(b+1),-1):
    print(a[i])
'''\
'''
a = [50,4,53,555,21,60,11.2,10]
l1 = [i for i in a if i % 2 == 0]

print(l1)
print(*l1[1:3])

'''\

'''
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # print(alphabet)
    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:', *filteredVowels)
# for vowel in filteredVowels:
    # print(vowel)
'''\
'''
a,b = input().split()
c = '.|.'
d = '-'
for i in range(1, a, 2):
    print(''.join(c * i).center(b , '-'))
print("WELCOME".center(b, '-'))
for i in range(a-2, -1, -2):
    print(''.join(c * i).center(b , '-'))
'''\
'''
a = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name , score])
print(a)
'''
a=[1,2,3,5,2,5]

a.remove(2)
print(a)