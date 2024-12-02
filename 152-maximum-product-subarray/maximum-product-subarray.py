class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = nums[0]
        currmin = nums[0]
        res = currmax
        for num in nums[1:]:
            temp = max(num, currmax*num, currmin*num)
            currmin = min(num, currmax*num, currmin*num)
            currmax = temp
            res = max(currmax, res)
        return res