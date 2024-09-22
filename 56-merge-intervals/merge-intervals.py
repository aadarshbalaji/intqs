class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        for arr in intervals[1:]:
            if arr[0] <= prev[1]:
                prev[1] = max(prev[1], arr[1])
            else:
                ans.append(prev)
                prev = arr
        ans.append(prev)
        return ans