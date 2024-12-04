class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currmin = prices[0]
        prof = 0
        for price in prices[1:]:
            if price > currmin:
                prof += price - currmin
            currmin = price
        return prof