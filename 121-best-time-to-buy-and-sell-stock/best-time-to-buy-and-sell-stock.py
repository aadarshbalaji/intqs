class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmax = 0
        currmin = prices[0]
        for p in prices[1:]:
            if p > currmin:
                currmax = max(currmax, p-currmin)
            else:
                currmin = p
        return currmax
