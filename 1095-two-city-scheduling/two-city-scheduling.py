class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        distances = [[x[0]-x[1], i] for i,x in enumerate(costs)]
        distances.sort(key=lambda x: abs(x[0]), reverse=True)
        ca = 0
        cb = 0
        total = 0
        n = len(costs)//2
        while ca < n and cb < n:
            diff, index = distances.pop(0)
            if diff > 0:
                cb += 1
                total += costs[index][1]
            else:
                ca += 1
                total += costs[index][0]
        if ca >= n:
            for v, index in distances:
                total += costs[index][1]
        else:
            for v, index in distances:
                total += costs[index][0]
        return total