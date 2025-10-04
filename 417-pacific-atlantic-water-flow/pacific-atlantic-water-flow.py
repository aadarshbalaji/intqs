class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        #find all pacific
        #find all atlantic
        #go upwards from pacific and atlantic and and then get union of this set
        for i in range(len(heights[0])):
            pacific.add((0,i))
            atlantic.add((len(heights)-1, i))

        for j in range(len(heights)):
            pacific.add((j,0))
            atlantic.add((j, len(heights[0]) -1))

        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        q = deque(pacific)
        while q:
            row, col = q.popleft()
            val = heights[row][col]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[nr][nc] >= val and (nr,nc) not in pacific:
                    pacific.add((nr,nc))
                    q.append((nr,nc))

        

        d = deque(atlantic)
        while d:
            row, col = d.popleft()
            val = heights[row][col]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[nr][nc] >= val and (nr,nc) not in atlantic:
                    atlantic.add((nr,nc))
                    d.append((nr,nc))

        
        return list(pacific & atlantic)
        


            