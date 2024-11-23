class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest, second = float('inf'), float('inf')
        for i, num in enumerate(nums):
            if num < smallest:
                smallest = num
            elif smallest < num < second:
                second = num
            elif smallest < second < num:
                return True
        return False
