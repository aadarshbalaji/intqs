class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rv = 0
        curr = prices[0]
        for p in prices[1:]:
            if p > curr:
                rv = max(rv, p-curr)
            else:
                curr = p
        return rv