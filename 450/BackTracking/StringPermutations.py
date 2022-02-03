def permutauion(arr, left, right):
    if left == right:
        print(''.join(arr))
        return
    
    for idx in range(left,right+1):
        # we swap the charters from left to end
        arr[idx],arr[left] = arr[left],arr[idx]

        # recurrsion relations
        permutauion(arr, left + 1, right)

        # undo the swap
        arr[idx],arr[left] = arr[left],arr[idx]

if __name__ == '__main__':
    string = input("Please enter the string")
    str_list = [a for a in string]
    left = 0
    right = len(str_list) - 1
    permutauion(str_list, left, right)
