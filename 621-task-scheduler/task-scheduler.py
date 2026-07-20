class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        for task, frequency in freq.items():
            heappush(heap, (-frequency, task))
        
        cooldown = deque()
        time = 0

        while heap or cooldown:
            if cooldown and cooldown[0][2] == time:
                letter, negcount, jail_time = cooldown.popleft()
                heappush(heap, (negcount, letter))
            if heap:
                negcount, letter = heappop(heap)
                real_count = -negcount -1
                if real_count > 0:
                    cooldown.append((letter, -real_count, time+n + 1))
            time += 1
        return time
            

