class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(heights)
        m = len(heights[0])
        atlantic = set()
        pacific = set()
        aq = deque()
        pq = deque()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        for x in range(n):
            pacific.add((x,0))
            pq.append((x,0))
            atlantic.add((x,m-1))
            aq.append((x,m-1))
        for col in range(m):
            pacific.add((0, col))
            pq.append((0,col))
            atlantic.add((n-1, col))
            aq.append((n-1,col))
        while aq:
            r, c = aq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and heights[nr][nc] >= heights[r][c] and (nr, nc) not in atlantic:
                    aq.append((nr,nc))
                    atlantic.add((nr,nc))
    
        while pq:
            r, c = pq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and heights[nr][nc] >= heights[r][c] and (nr, nc) not in pacific:
                    pq.append((nr,nc))
                    pacific.add((nr,nc))
        
        return list(set.intersection(pacific, atlantic))
        
        