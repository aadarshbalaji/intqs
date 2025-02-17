class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainders = {0:-1}
        currsum = 0
        for i in range(len(nums)):
            currsum += nums[i]
            remainder = currsum % k

            if remainder in remainders:
                if i-remainders[remainder] > 1:
                    return True
            else:
                remainders[remainder] = i
        return False