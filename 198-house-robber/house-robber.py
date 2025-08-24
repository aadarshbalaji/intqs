class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        dp[i] = max amount u can steal only using houses 0 -> i
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        '''
        dp = [0 for i in range(len(nums))]
        if len(nums) < 2:
            return nums[0] if nums else 0
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[len(nums)-1]

        