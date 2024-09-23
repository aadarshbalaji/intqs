class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(row, col, k):
            if k == len(word):
                return True
            
            if not (0 <= row < rows) or not (0 <= col < cols) or (row, col) in visited or board[row][col] != word[k]:
                return False

            visited.add((row, col))
            res = bfs(row, col + 1, k + 1) or bfs(row, col - 1, k + 1) or bfs(row + 1, col, k + 1) or bfs(row - 1, col, k + 1)
            visited.remove((row, col))
            return res


        '''count = defaultdict(int)
        for c in word:
            count[c] += 1
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]'''

        for r in range(rows):
            for c in range(cols):
                if bfs(r, c, 0):
                    return True
        return False