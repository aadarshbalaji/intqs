class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for c in tasks:
            freq[c] += 1
        
        heap = []
        timer = 0
        cooldown = deque()
        for key, val in freq.items():
            heappush(heap, -val)

        while heap or cooldown:
            if heap:
                task = -heappop(heap)
                if task > 1:
                    cooldown.append((task-1, timer+n+1))
            timer += 1
            while cooldown and cooldown[0][1] == timer:
                taskcount, nextiter = cooldown.popleft()
                heappush(heap, -taskcount)
        return timer
