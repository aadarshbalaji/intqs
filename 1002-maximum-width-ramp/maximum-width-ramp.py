class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        call = (list(range(len(nums))))
        call.sort(key = lambda x: nums[x])
        #print(call)
        currmin = float('inf')
        maxrange = 0
        for i in range(len(call)):
            maxrange = max(maxrange, call[i]-currmin)
            currmin = min(currmin, call[i])
        return maxrange