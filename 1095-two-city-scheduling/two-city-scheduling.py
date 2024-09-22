class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        greedy = [[x[0]-x[1], i] for i,x in enumerate(costs)]
        counta = 0
        countb = 0
        greedy.sort(key=lambda x: abs(x[0]), reverse=True)
        n = len(costs) // 2
        i = 0
        total = 0
        while counta < n and countb < n:
            diff, index = greedy[i]
            if diff > 0:
                total += costs[index][1]
                countb += 1
            else:
                total += costs[index][0]
                counta += 1
            i += 1
        if counta >= n:
            for d, index in greedy[i:]:
                total += costs[index][1]
        if countb >= n:
            for d, index in greedy[i:]:
                total += costs[index][0]
        return total