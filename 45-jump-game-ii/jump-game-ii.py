class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = minreach = maxreach = 0
        while maxreach < n-1:
            currfar = 0
            for i in range(minreach, maxreach+1):
                currfar = max(currfar, i + nums[i])
            count += 1
            minreach = maxreach + 1
            maxreach = currfar
        return count

