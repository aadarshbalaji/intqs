class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenrows = len(board)
        lencols = len(board[0])
        visited = set()
        def search(r, c, index):
            if index == len(word):
                return True
            if (r,c) in visited or not 0 <= r < lenrows or not 0 <= c <lencols or board[r][c] != word[index]:
                return False
            visited.add((r,c))
            rv = search(r+1, c, index+1) or search(r-1, c, index+1) or search(r, c-1, index+1) or  search(r, c+1, index+1)
            visited.remove((r,c))
            return rv



        for i in range(lenrows):
            for j in range(lencols):
                if board[i][j] == word[0]:
                    if search(i, j, 0):
                        return True
        return False
