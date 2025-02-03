class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmax = nums[0]
        currsum = nums[0]
        for num in nums[1:]:
            if currsum < 0:
                currsum = 0
            currsum += num
            currmax = max(currmax, currsum)
        return currmax
            