if __name__ == '__main__':
    out_list = []
    N = int(input())
    input_list = []
    for _ in range(N):
        input_list.append(input())
    for i in range(N):
        if 'insert' in input_list[i]:
            temp = input_list[i].split()
            out_list.insert(int(temp[1]), int(temp[2]))
        if 'print' in input_list[i]:
            print(out_list)
        if 'remove' in input_list[i]:
            temp = input_list[i].split()
            for j in out_list:
                if int(j) == int(temp[1]):
                    out_list.remove(j)
                    break
        if 'sort' in input_list[i]:
            temp = []
            for el in sorted(out_list):
                temp.append(el)
            out_list.clear()
            out_list = temp
        if 'append' in input_list[i]:
            temp = input_list[i].split()
            out_list.append(int(temp[1]))
        if 'pop' in input_list[i]:
            out_list.pop(-1)
        if 'reverse' in input_list[i]:
            tlist = [el for el in reversed(out_list)]
            out_list.clear()
            out_list = tlist
