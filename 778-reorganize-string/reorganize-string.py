class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        for c, times in freq.items():
            heappush(heap, [-times, c])
        
        currstr = ""
        if not heap:
            return ""
        currnotallowed = heappop(heap)
        currstr += currnotallowed[1]
        while len(currstr) != len(s):
            if not heap:
                return ""
            timesleft, newletter = heappop(heap)
            currstr += newletter
            if -1 * currnotallowed[0] > 1:
                heappush(heap, [currnotallowed[0]+1, currnotallowed[1]])
            currnotallowed = [timesleft, newletter]
        return currstr
            
            