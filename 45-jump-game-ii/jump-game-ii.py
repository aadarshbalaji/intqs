class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        minreach, maxreach = 0,0
        
        while maxreach < n - 1:
            currfar = 0
            for i in range(minreach, maxreach + 1):
                currfar = max(currfar, i + nums[i])
            count += 1
            minreach = maxreach + 1
            maxreach = currfar
        return count