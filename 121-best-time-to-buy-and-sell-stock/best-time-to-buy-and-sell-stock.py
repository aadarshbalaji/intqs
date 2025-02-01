class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        lowest = prices[0]
        for price in prices:
            maxprof = max(maxprof, price-lowest)
            lowest = min(lowest, price)
        return maxprof