
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in c.items()]
        heapify(maxheap)
        curr = ""
        while maxheap:
            if len(curr) == len(s):
                return curr
            negcount, letter = heappop(maxheap)
            if curr and letter == curr[-1]:
                if not maxheap:
                    return ''
                newnegcount, newletter = heappop(maxheap)
                curr += newletter
                if newnegcount < -1:
                    heappush(maxheap, [newnegcount +1, newletter])
            else:
                curr += letter
                negcount += 1
            if negcount <= -1:
                heappush(maxheap, [negcount, letter])
        
        return curr if len(curr) == len(s) else ''

        



