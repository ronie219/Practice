cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost.append(0)
memo = [-1] * len(cost)


def minimunCost(idx, cost):
    # Base condition
    if idx == 0 or idx == 1:
        return cost[idx]
    if memo[idx] != -1:
        return memo[idx]
    memo[idx] = cost[idx] + min(minimunCost(idx - 1, cost), minimunCost(idx - 2, cost))
    return memo[idx]


print(minimunCost(len(cost) - 1, cost))
