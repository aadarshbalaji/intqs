class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hs = Counter(tasks)
        heap = []
        timer = 0
        cooldown = deque()
        for num, count in hs.items():
            heappush(heap, -count)
        
        while heap or cooldown:
            if cooldown and cooldown[0][1] == timer:
                negcount, expectedtime = cooldown.popleft()
                heappush(heap, negcount)
            timer += 1
            if heap:
                negcount = heappop(heap)
                if negcount < -1:
                    cooldown.append([negcount+1, timer+n])
        
        return timer