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


