class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if (mid > 0 and nums[mid-1] != target) or mid == 0:
                    starting = mid
                    break
                else:
                    r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        ending = starting
        l = starting + 1
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if (mid < len(nums) - 1 and nums[mid+1] != target) or mid == len(nums) - 1:
                    ending = mid
                    break
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return [starting, ending]