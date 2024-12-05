class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenrows = len(board)
        lencols = len(board[0])
        visited = set()

        def search(index, i, j):
            if index == len(word):
                return True
            if not 0 <= i < lenrows or not 0 <= j < lencols or (i, j) in visited or board[i][j] != word[index]:
                return False
            visited.add((i,j))
            ans = search(index+1, i+1, j) or search(index+1, i-1, j) or search(index+1, i, j-1) or search(index+1, i, j+1)
            visited.remove((i,j))
            return ans


        for x in range(lenrows):
            for y in range(lencols):
                if board[x][y] == word[0]:
                    if search(0, x,y):
                        return True
        return False

