class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        target = n / 2
        hs = defaultdict(int)
        for num in nums:
            hs[num] += 1
            if hs[num] >= target:
                return num