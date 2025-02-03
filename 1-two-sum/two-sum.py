class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i, num in enumerate(nums):
            newtarget = target - num
            if newtarget in hs:
                return [i, hs[newtarget]]
            hs[num] = i
        
            
            