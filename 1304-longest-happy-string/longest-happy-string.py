class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        heap = []
        cooldown = deque()
        curr = ''
        if a > 0:
            heappush(heap, [-a, 'a'])
        if b > 0:
            heappush(heap, [-b, 'b'])
        if c > 0:
            heappush(heap, [-c, 'c'])

        while heap or cooldown:
            if len(heap) + len(cooldown) == 1:
                if heap and heap[0][1] + heap[0][1] == curr[-2:]:
                    break
                if cooldown and cooldown[0][1] + cooldown[0][1] == curr[-2:]:
                    break
            if cooldown and curr[-2:] != cooldown[0][1] + cooldown[0][1]:
                heappush(heap, cooldown.popleft())
            if heap:
                negcount, letter = heappop(heap)
                if curr[-2:] != letter + letter:
                    curr =  curr + letter
                    if negcount < -1:
                        heappush(heap, [negcount+1, letter])
                else:
                    cooldown.append([negcount, letter])
        return curr