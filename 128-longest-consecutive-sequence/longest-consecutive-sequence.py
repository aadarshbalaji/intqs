class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        currmax = 0
        for num in seen:
            if num - 1 not in seen:
                counter = 1
                while num + 1 in seen:
                    counter += 1
                    num += 1
                currmax = max(currmax, counter)
        return currmax
                