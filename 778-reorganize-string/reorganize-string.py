class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 0:
            return ''
        freq = Counter(s)
        heap = []
        for letter, count in freq.items():
            heappush(heap, [-count, letter])

        holdoff = None
        rv = ''
        while heap:
            putcount, putletter = heappop(heap)
            if holdoff and holdoff[0] < -1:
                heappush(heap, [holdoff[0] + 1, holdoff[1]])
            rv += putletter
            holdoff = [putcount, putletter]
        return rv if len(rv) == len(s) else ''