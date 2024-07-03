class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currbuy = prices[0]
        prof = 0
        for num in prices[1:]:
            if currbuy > num:
                currbuy = num
            prof = max(prof, num-currbuy)
        return prof

        
            