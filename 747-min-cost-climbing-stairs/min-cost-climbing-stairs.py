class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):  
            if n < 2: 
                return cost[n] 
            if n not in memo:
                memo[n] = cost[n] + min(dp(n-1), dp(n-2))
            return memo[n]
        memo = {}
        length = len(cost) 
        return min(dp(length-1), dp(length-2))
            