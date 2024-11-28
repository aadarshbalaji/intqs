class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hs = defaultdict(lambda x: -1)
        for i, num in enumerate(nums):
            if num in hs:
                if i - hs[num] <= k:
                    return True
            hs[num] = i
        return False