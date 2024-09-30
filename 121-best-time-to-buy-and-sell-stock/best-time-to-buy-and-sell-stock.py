class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currdiff = 0
        currmin = prices[0]
        for num in prices:
            if num > currmin:
                currdiff = max(currdiff, num-currmin)
            else:
                currmin = num
        return currdiff