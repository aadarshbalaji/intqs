class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        maxcount = -1
        maxvar = -1
        for val, count in c.items():
            if val % 2 == 0:
                if count > maxcount:
                    maxcount = count
                    maxvar = val
                elif count == maxcount:
                    maxvar = min(maxvar, val)
        return maxvar
