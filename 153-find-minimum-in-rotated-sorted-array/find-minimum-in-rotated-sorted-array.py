class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            index = left + (right - left)//2
            val = nums[index]
            if val < nums[right]:
                right = index
            else:
                left = index + 1
        return nums[left]