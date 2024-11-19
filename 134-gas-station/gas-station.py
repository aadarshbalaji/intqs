class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        currgas = 0
        start = 0
        i = 0
        while i < len(gas) - 1:
            currgas += gas[i] - cost[i]
            if currgas < 0:
                currgas = 0
                start = i + 1
            i += 1
        return start