class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for num in num_set:
            if num-1 not in num_set:
                currcount = 0
                curr = num
                while curr in num_set:
                    currcount += 1
                    curr += 1
                count = max(count, currcount)
        return count
