class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rv = nums[0]
        currmin = 1
        currmax = 1
        for num in nums:
            temp = num * currmax
            currmax = max(num, num*currmin, num*currmax)
            currmin = min(num, currmin*num, temp)
            rv = max(rv, currmax)
        return rv
