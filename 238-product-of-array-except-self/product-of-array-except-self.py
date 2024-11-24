class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        premul = [1] * n
        postmul = [1] * n
        rv = [0] * n
        for i in range(1, n):
            premul[i] = premul[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            postmul[i] = postmul[i+1] * nums[i+1]
        
        for i in range(n):
            rv[i] = premul[i] * postmul[i]
        return rv