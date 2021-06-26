def reverse_array(array,start,end):
    while start < end:
        array[start],array[end] = array[end],array[start]
        start +=1
        end -=1
    return array


A = [1, 2, 3, 4, 5, 6, 7]
print(A)
reverse = reverse_array(A, 0, 6)
print("Reversed list is")
print(reverse)