class Solution:
    def jump(self, nums: List[int]) -> int:
        near = 0
        far = 0
        steps = 0
        while far < len(nums) - 1:
            curr = 0
            for i in range(near, far+1):
                curr = max(curr, i + nums[i])
            near = far + 1
            far = curr
            steps += 1
        return steps            
