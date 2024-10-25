class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            dp[i] = amount+1
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        #print(dp)
        return dp[-1] if dp[-1] != amount + 1 else -1
                        