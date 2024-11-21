class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        l = 0
        currmax = 0
        for r in range(len(right_max)):

            while l < r and nums[l] > right_max[r]:
                l += 1
            currmax = max(currmax, r-l)
        return currmax