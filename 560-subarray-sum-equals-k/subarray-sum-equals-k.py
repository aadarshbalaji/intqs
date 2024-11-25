class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        hs = defaultdict(int)
        hs[0] = 1
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - k in hs:
                count += hs[prefix_sum - k]
            hs[prefix_sum] += 1
        return count