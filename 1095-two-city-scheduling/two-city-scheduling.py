class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0]-x[1])
        ans = 0
        for i in range(len(costs)//2):
            ans += costs[i][0]
            ans += costs[len(costs)-i-1][1]
        return ans