class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for c in tasks:
            freq[c] += 1
        
        heap = []
        timer = 0
        cooldown = deque()
        for item, f in freq.items():
            heappush(heap, -f)

        while heap or cooldown:
            if heap: 
                currtasks = -heappop(heap)
                if currtasks > 1:
                    cooldown.append((currtasks-1, n + timer + 1))
            timer += 1

            if cooldown and cooldown[0][1] == timer:
                amount, newtime = cooldown.popleft()
                heappush(heap, -amount)
        return timer
