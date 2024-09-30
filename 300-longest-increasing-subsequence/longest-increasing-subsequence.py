class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
                continue
            index = bisect_left(res, num)
            res[index] = num
        return len(res)