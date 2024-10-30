class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
            else:
                index = bisect_left(res, num)
                res[index] = num
        return len(res)