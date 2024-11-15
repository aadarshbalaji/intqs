class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        new = ''
        heap = []
        for letter, count in freq.items():
            heappush(heap, [-count, letter])
        
        if heap:
            first = heappop(heap)
            new += first[1]
            temp = [first[0] + 1, first[1]]

        while heap:
            curr = heappop(heap)
            new += curr[1]
            if temp[0] < 0:
                heappush(heap, temp)
            temp = [curr[0] + 1, curr[1]]
        if len(new) == len(s):
            return new
        else:
            return ''