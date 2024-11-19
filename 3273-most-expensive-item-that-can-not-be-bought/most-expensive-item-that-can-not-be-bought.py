class Solution(object):
    def mostExpensiveItem(self, primeOne, primeTwo):
        """
        :type primeOne: int
        :type primeTwo: int
        :rtype: int
        """
        dp = [False] * (primeOne * primeTwo)
        dp[0] = True
        currmax = 0
        for i in range(1, primeOne * primeTwo):
            if (i - primeOne >= 0 and dp[i-primeOne]) or (i - primeTwo >= 0 and dp[i-primeTwo]):
                dp[i] = True
            else:
                currmax = i
        return currmax
            