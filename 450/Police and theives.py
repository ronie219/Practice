def catchThevies(arr, k):
    caught = set()
    count = 0
    for idx in range(len(arr)):
        flag = False
        if arr[idx] == "P":
            # check backword
            for t in range(idx - 1, idx - k - 1, -1):
                if t < 0:
                    flag = True
                    break
                if arr[t] == "T" and t not in caught:
                    caught.add(t)
                    count += 1
                    break
            else:
                flag = True
            if flag:
                for t in range(idx + 1, idx + k + 1):
                    if t > len(arr) - 1:
                        break
                    if arr[t] == "T" and t not in caught:
                        caught.add(t)
                    count += 1
                    break
    print(count)


arr = ["T", "T", "P", "P", "T", "P"]
catchThevies(arr, 2)
