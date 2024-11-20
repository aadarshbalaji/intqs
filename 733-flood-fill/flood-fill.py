class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        visited = set()
        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color
        while q:
            row, col = q.popleft()
            visited.add((row,col))
            for dr, dc in [[0,1], [0,-1],[1,0],[-1,0]]:
                newrow, newcol = row + dr, col + dc
                if (newrow, newcol) not in visited and 0 <= newrow < len(image) and 0 <= newcol < len(image[0]) and image[newrow][newcol] == target:
                  q.append((newrow, newcol))
                  image[newrow][newcol] = color
            
        
        return image