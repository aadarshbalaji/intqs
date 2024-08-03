class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        startz = cost
        starto = cost[1:]
        memo = {}
        def mincost(arr):
            if len(arr) == 0:
                return 0
            if len(arr) < 3:
                return arr[0]
            if str(arr) not in memo.keys():
                memo[str(arr)] = arr[0] + min(mincost(arr[1:]), mincost(arr[2:]))
            return memo[str(arr)]
        return min(mincost(startz), mincost(starto))
            