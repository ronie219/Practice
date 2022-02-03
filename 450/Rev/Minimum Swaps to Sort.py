def minSwaps(arr):
    aux = []
    swap = 0
    for idx in range(len(arr)):
        aux.append((arr[idx], idx))
    aux.sort(key=lambda x: x[0])

    visited = [False for _ in range(len(arr))]
    for idx in range(len(arr)):
        if aux[idx][1] == idx or visited[idx] == True:
            continue
        clen = 0
        swapidx = idx
        while not visited[swapidx]:
            visited[swapidx] = True
            clen += 1
            swapidx = aux[swapidx][1]
        swap += clen - 1

    return swap


if __name__ == '__main__':
    arr = [10, 19, 6, 3, 5]
    print(minSwaps(arr))
