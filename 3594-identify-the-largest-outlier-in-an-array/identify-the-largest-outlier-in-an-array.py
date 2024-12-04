class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqs = Counter(nums)
        total = sum(nums)
        maxlargest = -float('inf')
        for num in nums:
            outlier = total - 2*num
            if outlier in freqs and (freqs[outlier] > 1 or outlier != num):
                maxlargest = max(maxlargest, outlier)
        return maxlargest
        