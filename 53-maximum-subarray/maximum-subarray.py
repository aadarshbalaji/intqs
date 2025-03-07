class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSum = nums[0]
        currsum = nums[0]

        for num in nums[1:]:
            if currsum < 0:
                currsum = 0
            currsum += num
            maxSum = max(maxSum, currsum)
        return maxSum
            



