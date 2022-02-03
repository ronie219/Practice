from turtle import back


def productExceptSelf(nums, n):
    # without using division method
    forward = [1 for _ in range(n)]
    backward = [1 for _ in range(n)]

    # for filling the forward array
    for idx in range(1, n):
        forward[idx] = nums[idx-1] * forward[idx - 1]

    # for filling the backward array
    for idx in range(n-2, -1, -1):
        backward[idx] = nums[idx+1] * backward[idx + 1]

    final_product = []
    for idx in range(n):
        final_product.append(forward[idx] * backward[idx])

    return final_product


if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    print(productExceptSelf(arr, len(arr)))
