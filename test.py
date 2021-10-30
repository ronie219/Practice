<<<<<<< HEAD
input = "['ab' , 'cd', 1, 'ef']"

# out = []
# print(input[1:-1])
#
# for val in input[1:-1].split(','):
#     print(val)
#     out.append(val)
#
# print(out)
out = []
input = input[1:-1].split(",")
for item in input:
    item=item.strip()
    try:
        out.append(int(item))
    except:
        print(item)
        out.append(item[1:-1])
print(out)


=======
input = "['ab' , 'cd', 1, 'ef']"

# out = []
# print(input[1:-1])
#
# for val in input[1:-1].split(','):
#     print(val)
#     out.append(val)
#
# print(out)
out = []
input = input[1:-1].split(",")
for item in input:
    item=item.strip()
    try:
        out.append(int(item))
    except:
        print(item)
        out.append(item[1:-1])
print(out)


>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a
