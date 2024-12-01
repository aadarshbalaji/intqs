class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = set()
        for num in nums:
            if num in hs:
                return num
            hs.add(num)
        