class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = set(nums)
        maxlen = 0
        for num in nums:
            if num - 1 not in hs:
                start = num
                while num in hs:
                    num += 1
                maxlen = max(maxlen, num - start)
        return maxlen