class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentmax = nums[0]
        currentsub = nums[0]
        for num in nums[1:]:
            if currentsub < 0:
                currentsub = 0
            currentsub += num
            currentmax = max(currentsub, currentmax)
        return currentmax