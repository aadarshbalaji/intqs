class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                currsum = nums[l] + nums[r] + nums[i]
                if abs(target-currsum) < abs(target-closest):
                    closest = currsum
                if currsum == target:
                    return currsum
                if currsum < target:
                    l += 1
                    continue
                if currsum > target:
                    r -= 1
                    continue
        return closest
                

