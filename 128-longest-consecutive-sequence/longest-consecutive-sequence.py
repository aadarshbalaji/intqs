class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pog = nums[:]
        if len(nums) == 0:
            return 0
        count = 1
        maxcount = 1
        heapq.heapify(pog)
        preval = heapq.heappop(pog)
        while len(pog) > 0:
            val = heapq.heappop(pog)
            #print(val, count)
            if val - preval == 0:
                continue
            if val - preval == 1:
                count += 1
            else:
                count = 1
            maxcount = max(count, maxcount)
            preval = val

        return maxcount