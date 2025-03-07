class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        def helper(arr):
            dp = [0 for i in range(len(arr))]
            if len(arr) < 3:
                return max(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for j in range(2, len(arr)):
                dp[j] = max(dp[j-1], dp[j-2] + arr[j])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))

        