class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapp = {}
        for i in range(len(nums)):
            score = target - nums[i]
            if score in mapp.keys():
                return [mapp[score], i]
            mapp[nums[i]] = i
            