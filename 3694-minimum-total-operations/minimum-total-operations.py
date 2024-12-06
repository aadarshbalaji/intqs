class Solution:
    def minOperations(self, nums: List[int]) -> int:
        countdiffs = 0
        prev = nums[-1]
        for num in nums[-2::-1]:
            if prev != num:
                countdiffs += 1
            prev = num
        return countdiffs
        '''wow = 0
        prev = nums[0]
        for x in nums[1:]:
            if prev != x:
                wow += 1
            prev = x
        return min(countdiffs, wow)'''