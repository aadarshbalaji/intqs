class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robsimple(arr):
            if len(arr) < 3:
                return max(arr)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
            return dp[-1]



        return max(robsimple(nums[1:]), robsimple(nums[:-1]))