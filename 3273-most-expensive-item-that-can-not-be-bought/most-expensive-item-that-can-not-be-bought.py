class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        dp = [0] * (primeOne * primeTwo)
        dp[primeOne] = 1
        dp[primeTwo] = 1
        for i in range(len(dp)):
            if i + primeOne < len(dp) and dp[i]:
                dp[i+primeOne] = 1
            if i + primeTwo < len(dp) and dp[i]:
                dp[i+primeTwo] = 1
        
        for i in range(len(dp)-1,-1,-1):
            if not dp[i]:
                return i
            
        