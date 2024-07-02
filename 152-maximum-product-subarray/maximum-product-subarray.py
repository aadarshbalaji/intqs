class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curmin = 1
        curmax = 1
        for num in nums:
            temp = curmax * num
            curmax = max(num, num * curmin, num * curmax)
            curmin = min(num, num * curmin, temp)
            result = max(curmax, result)
        return result