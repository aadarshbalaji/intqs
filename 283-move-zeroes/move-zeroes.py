class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[place], nums[i] = nums[i], nums[place]
                place += 1
        