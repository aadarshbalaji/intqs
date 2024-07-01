class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(smol):
            r1,r2 = 0,0
            for num in smol:
                temp = max(num + r1, r2)
                r1 = r2
                r2 = temp
            return r2
        return max(nums[0] + rob1(nums[2:len(nums)-1]), rob1(nums[1:]))