class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hs = defaultdict(int)
        for c in s:
            hs[c] += 1
        
        heap = []
        for letter, count in hs.items():
            heappush(heap, [-count, letter])
        
        s = ""
        while heap:
            c, l = heappop(heap)
            s = s + l * -c
        return s
        