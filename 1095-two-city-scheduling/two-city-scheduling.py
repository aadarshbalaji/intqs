class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        costs.sort(key = lambda x: x[0]-x[1])
        total = 0
        n = len(costs)//2
        for i in range(n):
            total += costs[i][0]
            total += costs[n+i][1]
        return total