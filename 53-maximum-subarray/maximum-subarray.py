class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curr = nums[0]
        for num in nums[1:]:
            if curr < 0:
                curr = 0
            curr += num
            res = max(curr, res)
        return max(res, curr)