class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        def test(val):
            index = 0
            count = 0
            while index < n-1:
                if nums[index+1]-nums[index] <= val:
                    count += 1
                    index += 2
                else:
                    index += 1
            return count >= p
        
        l = 0
        r = nums[-1]-nums[0]
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                r = mid
            else:
                l = mid + 1
        return l