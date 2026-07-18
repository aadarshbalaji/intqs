class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1 for i in range(len(nums))]
        suffix_arr = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1,-1):
            suffix_arr[i] = suffix_arr[i+1] * nums[i+1]
        
        return [i*j for i,j in zip(prefix_arr, suffix_arr)]



        
        