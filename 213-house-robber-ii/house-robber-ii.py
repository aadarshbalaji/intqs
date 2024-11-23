class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        def robsimple(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2,len(arr)):
                dp[i] = max(dp[i-2]+arr[i], dp[i-1])
            return dp[-1]
        return max(robsimple(nums[1:]), robsimple(nums[:-1]))