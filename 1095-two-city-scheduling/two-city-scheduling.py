class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        totalcosts = 0
        for i in range(len(costs)//2):
            totalcosts += costs[i][0]
            totalcosts += costs[len(costs)-1-i][1]
        return totalcosts