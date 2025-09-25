class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        numrows = len(rooms)
        numcols = len(rooms[0])
        q = deque()
        walls = set()
        for i in range(numrows):
            for j in range(numcols):
                if rooms[i][j] == 0:
                    q.append((i,j,0))
                if rooms[i][j] == -1:
                    walls.add((i,j))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r, c, so_far = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < numrows and 0 <= nc < numcols and (nr, nc) not in walls:
                    if rooms[nr][nc] == 2147483647:
                        q.append((nr,nc,so_far + 1))
                    rooms[nr][nc] = min(rooms[nr][nc], so_far+1)
        

            

        