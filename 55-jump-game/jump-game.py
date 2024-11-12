class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        lastseen = len(nums) - 1
        for i in range(len(nums)-2, -1,-1):
            if i + nums[i] >= lastseen:
                lastseen = i
        return lastseen == 0