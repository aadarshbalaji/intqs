class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # freqs = {}
        # for task in tasks:
        #     freqs[task] = freqs.get(task, 0) + 1

        freqs = Counter(tasks)
        heap = []
        for letter, count in freqs.items():
            heappush(heap, -count)
        cooldown = deque()
        timer = 0
        while heap or cooldown:
            if cooldown and cooldown[0][1] == timer:
                negcount, expected = cooldown.popleft()
                heappush(heap, negcount)
            timer += 1
            if heap:
                negcount = heappop(heap)
                if negcount < - 1:
                    cooldown.append([negcount+1, timer + n])
                    
        return timer
