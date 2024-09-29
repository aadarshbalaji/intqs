class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i, num in enumerate(nums):
            if not res or res[-1] < num:
                res.append(num)
            else:
                index = bisect_left(res, num)
                res[index] = num
        return len(res)
            