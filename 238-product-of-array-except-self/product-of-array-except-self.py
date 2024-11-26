class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        rv = []
        for i, j in zip(prefix, suff):
            rv.append(i*j)
        return rv