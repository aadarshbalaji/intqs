class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(index, x, y, visited):
            #print(index, x, y, visited)
            if index >= len(word):
                return True
            #print(word[index], x, y, visited)
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index] or (x, y) in visited:
                return False
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            visited.add((x, y))
            for dx, dy in directions:
                if search(index+1, x+dx, y+dy, visited):
                    return True
            visited.remove((x,y))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(0, i,j, set()):
                        return True
        return False
