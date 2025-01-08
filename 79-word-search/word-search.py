class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        lenrows = len(board)
        lencols = len(board[0])

        def search(index, r, c, visited):
            #print(index, r, c, visited)
            if word[index] != board[r][c]:
                return False
            if index == len(word) -1:
                return True
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < lenrows and 0 <= nc < lencols and (nr, nc) not in visited and word[index+1] == board[nr][nc]:
                    if search(index + 1, nr, nc, visited):
                        return True
                    visited.remove((nr,nc))
            return False

        for row in range(lenrows):
            for col in range(lencols):
                if board[row][col] == word[0]:
                    if search(0, row, col, set()):
                        return True
        return False
