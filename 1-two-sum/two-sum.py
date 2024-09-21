class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i, num in enumerate(nums):
            if target-num in hs:
                return [i, hs[target-num]]
            else:
                hs[num] = i

        