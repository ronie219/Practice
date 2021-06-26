# a, e , i, o, u,
def countVowelStrings(n):
    base_case = [[5, 4, 3, 2, 1]]
    if n == 1:
        return base_case[0][0]
    for _ in range(1, n):
        case = [0, 0, 0, 0, 1]
        idx = 3
        while idx >= 0:
            case[idx] = case[idx + 1] + base_case[-1][idx]
            idx -= 1
        base_case.append(case)
    print(base_case)


countVowelStrings(3)
