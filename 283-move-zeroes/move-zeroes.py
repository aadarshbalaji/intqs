class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        place = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[place], nums[i] = num, nums[place]
                place += 1
