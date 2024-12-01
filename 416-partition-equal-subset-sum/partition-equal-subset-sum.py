class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for num in nums[::-1]:
            nextdp = set()
            for t in dp:
                nextdp.add(t+num)
                nextdp.add(t)
            dp = nextdp
            if target in dp:
                return True
        return False