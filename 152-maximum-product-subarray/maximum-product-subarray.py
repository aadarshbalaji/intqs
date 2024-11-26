class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxsofar = nums[0]
        minsofar = nums[0]
        res = maxsofar
        for num in nums[1:]:
            temp = max(minsofar*num, num, maxsofar*num)
            minsofar = min(minsofar*num, num, maxsofar*num)
            maxsofar = temp
            res = max(res, maxsofar)
        return res