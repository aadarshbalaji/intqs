class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calc(m):
            c = 0
            for i, num in enumerate(nums):
                c += abs(m-num) * cost[i]
            return c
        l = min(nums)
        r = max(nums) + 1
        mid = (r+l)//2 
        while l < r:
            if calc(mid+1) > calc(mid):
                r = mid
            else:
                l = mid + 1
            mid = (r+l)//2 
        return calc(l)