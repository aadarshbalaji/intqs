class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currsum = nums[0]
        for num in nums[1:]:
            if currsum < 0:
                currsum = 0
            currsum += num
            maxsub = max(currsum, maxsub)
        return maxsub