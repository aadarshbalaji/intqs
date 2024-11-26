class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
         
        for i in range(amount+1):
            if dp[i] < float('inf'):
                for coin in coins:
                    if i + coin < len(dp):
                        dp[i+coin] = min(dp[i+coin], dp[i]+1)
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
            