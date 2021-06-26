# array = [6, -3, -10, 0, 2]
# array = [-8, 5, 3, 1, 6]
array = [6, -3, -10, 0, 2]
answer = array[0]
maximum_product = array[0]
minimum_product = array[0]

for arr in array[1:]:
    current_max_product = max(maximum_product * arr, arr, minimum_product * arr)
    current_min_product = min(maximum_product * arr, arr, minimum_product * arr)
    answer = max(answer, current_max_product)
    minimum_product = current_min_product
    maximum_product = current_max_product

print(answer)