class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        def helper(arr):
            if not arr:
                return 0
            dp = [0] * len(arr)
            dp[0] = arr[0]
            for i in range(1, len(arr)):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))
            
        
