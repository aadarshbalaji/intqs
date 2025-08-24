class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_helper(arr):
            dp = [0 for i in range(len(arr))]
            if len(arr) < 3:
                return max(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]
        if len(nums) < 3:
            return max(nums)
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1])) 
            