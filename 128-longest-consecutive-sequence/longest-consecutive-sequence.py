class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0

        for num in num_set:
            if num-1 not in num_set:
                starting = num
                curr = 1
                while starting+1 in num_set:
                    curr += 1
                    starting += 1
                count = max(count, curr)
        return count
