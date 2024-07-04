class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums) - 1
        i = 0
        if len(nums) == 1:
            return True
        while nums[i] != 0:
            if i >= final:
                return True
            new = 0
            for j in range(0,nums[i]):
                j += 1
                if i + j >= final:
                    return True
                if nums[i+j] > (nums[i]-j):
                    new = i + j
                    break
            if new != 0:
                i = new
            else:
                i += nums[i]
        return False
