from _collections import OrderedDict

item_list = OrderedDict()

for _ in range(int(input())):
    item = input().split()
    price = item.pop()
    if ' '.join(item) in item_list.keys():
        item_list[' '.join(item)] += int(price)
    else:
        item_list[' '.join(item)] = int(price)

[print(item, price) for (item,price) in item_list.items()]
