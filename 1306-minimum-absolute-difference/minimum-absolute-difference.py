class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        result = defaultdict(list)
        for i in range(len(arr)-1):
            result[abs(arr[i]-arr[i+1])].append([arr[i], arr[i+1]])
        x = min(result.keys())
        return result[x]