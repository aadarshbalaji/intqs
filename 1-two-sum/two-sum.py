class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hs = {}
        for i, num in enumerate(nums):
            newtarget = target - num
            if newtarget in hs:
                return [i, hs[newtarget]]
            hs[num] = i
        