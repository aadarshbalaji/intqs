class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestsum = float('inf')
        for i in range(len(nums)-1):
            currsum = 0
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currsum = nums[i] + nums[r] + nums[l]
                #print(currsum)
                if abs(target-currsum) < abs(target-closestsum):
                    closestsum = currsum
                if target == currsum:
                    return currsum
                elif currsum < target:
                    l += 1
                else:
                    r -= 1
        return closestsum