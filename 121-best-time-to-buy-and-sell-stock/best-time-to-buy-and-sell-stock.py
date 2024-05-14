class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        b = prices[0]
        for i in range(1, len(prices)):
            b = min(b, prices[i])
            m = max(m, prices[i] - b)
        return m