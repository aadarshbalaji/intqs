class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            lowercurr = table.get(num-1, 0)
            uppercurr = table.get(num+1, 0)
            value = lowercurr + uppercurr + 1
            table[num-lowercurr] = value
            table[num+uppercurr] = value
            maxval = max(maxval, value)
        return maxval