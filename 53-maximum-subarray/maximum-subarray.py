class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rv = nums[0]
        curr = nums[0]
        for num in nums[1:]:
            if curr < 0:
                curr = 0
            curr += num
            rv = max(curr, rv)
        return rv
