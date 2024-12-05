class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        counter = Counter(nums)
        maxoutlier = -float('inf')
        for num in nums:
            outlier = total - 2*num
            if outlier in counter:
                if outlier != num or counter[outlier] > 1:
                    maxoutlier = max(outlier, maxoutlier)
        return maxoutlier