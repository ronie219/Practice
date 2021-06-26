# Question 1
a = [1,2,3,4,5,6]
n = 2
new_list = []
for i in range(-n, len(a)-n, 1):
    new_list.append(a[i])
print(new_list)

# Question 3
from functools import reduce

a = 'Vrphwklqj phdqlqjixo'
a = a.replace('D','V')
a = a.replace('d','a')
a = a.replace('P','M')
a = a.replace('A','X')
a = a.replace('a','x')
print(a)

#Question 4
a = input("Enter a String")
b = ''
a = a.split(' ')
print(a)
for i in a:
    print(i)
    for j in range(-1,-(len(i)) - 1,-1):
        b = b + str(a[j])


print(str(b))

# Question 2
a = "abhishek"
print("The original string : " + str(a))
b = reduce(lambda x, y: x + y, sorted(a))
print("String after sorting : " + str(b))
###################################################
a = ['abhi','biswas','aakash']
b = []
for i in sorted(a):
    b.append(i)
print(b)