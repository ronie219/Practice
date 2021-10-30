from collections import deque


class Solution:

    # Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, n):
        n += 1
        KnightPos = tuple(KnightPos)
        queue = deque()
        visited = set()
        queue.append(KnightPos)
        track = {KnightPos: 0}
        while queue:
            var = queue.popleft()
            if var == tuple(TargetPos):
                return track[var]
            x = var[0]
            y = var[1]
            visited.add(var)
            if 0 < x + 2 < n and 0 < y - 1 < n and (x + 2, y - 1) not in visited:
                queue.append((x + 2, y - 1))
                track[(x + 2, y - 1)] = track[var] + 1

            if 0 < x + 2 < n and 0 < y + 1 < n and (x + 2, y + 1) not in visited:
                queue.append((x + 2, y + 1))
                track[(x + 2, y + 1)] = track[var] + 1

            if 0 < x - 2 < n and 0 < y + 1 < n and (x - 2, y + 1) not in visited:
                queue.append((x - 2, y + 1))
                track[(x - 2, y + 1)] = track[var] + 1

            if 0 < x - 2 < n and 0 < y - 1 < n and (x - 2, y - 1) not in visited:
                queue.append((x - 2, y - 1))
                track[(x - 2, y - 1)] = track[var] + 1

            if 0 < x - 1 < n  and 0 < y + 2 < n and (x - 1, y + 2) not in visited:
                queue.append((x - 1, y + 2))
                track[(x - 1, y + 2)] = track[var] + 1

            if 0 < x + 1 < n and 0 < y + 2 < n and (x + 1, y + 2) not in visited:
                queue.append((x + 1, y + 2))
                track[(x + 1, y + 2)] = track[var] + 1

            if 0 < x + 1 < n and 0 < y - 2 < n and (x + 1, y - 2) not in visited:
                queue.append((x + 1, y - 2))
                track[(x + 1, y - 2)] = track[var] + 1

            if 0 < x - 1 < n and 0 < y - 2 < n and (x - 1, y - 2) not in visited:
                queue.append((x - 1, y - 2))
                track[(x - 1, y - 2)] = track[var] + 1


if __name__ == '__main__':
    T=int(input("Enter T"))

    for i in range(T):
        N = int(input("ENter N"))
        KnightPos = list(map(int, input(" Knight").split()))
        TargetPos = list(map(int, input("target").split()))

        obj = Solution()
        ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
        print(ans)

