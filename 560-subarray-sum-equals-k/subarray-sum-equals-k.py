class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr = 0
        hs = defaultdict(int)
        hs[0] = 1
        for i, num in enumerate(nums):
            if curr + num - k in hs:
                count += hs[curr+num-k]
            hs[curr+num] += 1
            curr = curr + num
        return count
