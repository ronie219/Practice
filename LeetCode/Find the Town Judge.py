class Solution:
    def findJudge(self, N, trust):
        trusts  = [0] * N
        trusted = [0] * N
        for i in trust:
            trusts[i[0]-1] += 1
            trusted[i[1]-1] += 1
        judge = []
        count = 1
        for i,j in zip(trusts,trusted):
            if i == 0 and j == N-1:
                judge.append(count)
            count += 1
        return (judge[0]) if len(judge) == 1 else (-1)

s = Solution()
s.findJudge(3,[[1,3],[2,3],[3,1]])