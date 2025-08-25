class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.rowsum = [0 for i in range(n)]
        self.colsum = [0 for i in range(n)]
        self.firstdiag = 0
        self.seconddiag = 0
        self.infirstdiag = set((i,i) for i in range(n))
        self.inseconddiag = set()
        i = 0
        while i < n:
            self.inseconddiag.add((i, n-i-1))
            i += 1
        self.n = n

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            self.rowsum[row] += 1
            self.colsum[col] += 1
            if (row,col) in self.infirstdiag:
                self.firstdiag += 1
            if (row, col) in self.inseconddiag:
                self.seconddiag += 1
        else:
            self.rowsum[row] -= 1
            self.colsum[col] -= 1
            if (row,col) in self.infirstdiag:
                self.firstdiag -= 1
            if (row, col) in self.inseconddiag:
                self.seconddiag -= 1
        #print(self.inseconddiag)
        if abs(self.rowsum[row]) == self.n or abs(self.colsum[col]) == self.n or abs(self.firstdiag) == self.n or abs(self.seconddiag) == self.n:
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)