class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currplace = 0
        count = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[currplace], nums[i] = nums[i], nums[currplace]
                currplace += 1
            else:
                count += 1
                currplace = min(currplace, i)
        return len(nums) - count
