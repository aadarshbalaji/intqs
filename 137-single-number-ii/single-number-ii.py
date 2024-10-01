class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        for key in hm:
            if hm[key] != 3:
                return key
        
        
