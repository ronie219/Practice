arr = [2,6,1,9,4,5,3]
hash_set = {*arr}
longest_subsequence = 1
for i in arr:
    current_element = i
    count = 1
    if current_element - 1 not in hash_set:
        while current_element in hash_set:
            if longest_subsequence < count:
                longest_subsequence = count
            count += 1
            current_element += 1
print(longest_subsequence)