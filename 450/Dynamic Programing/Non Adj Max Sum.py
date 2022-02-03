"""
1. You are given a number n, representing the count of elements.
2. You are given n numbers, representing n elements.
3. You are required to find the maximum sum of a subsequence with no adjacent elements.

"""


def max_sum(arr):

    # taking two varibale inculde and exclude it will keep if we exculde the last element what will the max sum and vice a versa

    include = arr[0]
    exclude = 0

    for idx in range(1, len(arr)):
        # if we have to exclude the current item we have to option,
        # 1. we can chose from the last exculde and include we will choose the max
        # 2. if we have to include the current item then we have to choose the sum of exclude of previous one.
        temp = include
        include = exclude + arr[idx]
        exclude = max(temp, exclude)
    print(max(include, exclude))


if __name__ == '__main__':
    arr = [5, 10, 10, 100, 5]
    max_sum(arr)
