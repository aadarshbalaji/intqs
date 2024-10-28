class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l, r)
            snuff = (l+r)//2
            mid = nums[snuff]
            print(snuff)
            if r - l <= 2:
                return min(nums[l:r+1])
            if nums[l] < mid:
                if nums[l] < nums[r]:
                    r = snuff 
                else:
                    l = snuff 
            else:
                if nums[r] < nums[l]:
                    r = snuff 
                else:
                    l = snuff 
        
            
                    