from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data_zip = list(zip(startTime, endTime, profit))
        data_zip.sort(key=lambda x:x[0])

        def get_eligible_idx(idx, target):
            first = idx
            last = len(data_zip) - 1
            result = len(data_zip)
            while first <= last:
                mid = (last+first) // 2
                if data_zip[mid][0] >= target:
                    result=mid
                    last = mid - 1
                else:
                    first = mid + 1
            return result
        def solve(idx):
            if idx >= len(data_zip): return 0
            # take the current idx
            eligible_idx = get_eligible_idx(idx+1, data_zip[idx][1])
            taken = data_zip[idx][2] + solve(eligible_idx)
            not_taken = solve(idx+1)
            return max(taken,not_taken)
        return solve(0)


print(Solution().jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))