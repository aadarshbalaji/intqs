class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefixsum = 0
        hs = defaultdict(int)
        hs[0] = 1
        pre = [0] * (len(nums)+1)
        for i, num in enumerate(nums):
            prefixsum += num
            if prefixsum - k in hs:
                count += hs[prefixsum - k]
            hs[prefixsum] += 1
        return count
                