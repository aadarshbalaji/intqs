class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hs = defaultdict(int)
        hs[0] = 1
        count = 0
        for num in nums:
            prefix_sum += num
            count += hs[prefix_sum - k]
            hs[prefix_sum] += 1
        return count