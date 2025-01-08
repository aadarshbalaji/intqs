class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlen = 1
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                continue
            else:
                temp = num + 1
                count = 1
                while temp in nums:
                    count += 1
                    temp += 1
                    maxlen = max(maxlen, count)
        return maxlen