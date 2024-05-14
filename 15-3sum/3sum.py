class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                #print(left, right)
                if nums[left] + nums[right] == -nums[i]:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return res

        