class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
