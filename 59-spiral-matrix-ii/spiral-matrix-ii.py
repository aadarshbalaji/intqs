class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        tf = [[0] * n for i in range(n)]
        sample = [[False] * n for i in range(n)]
        def checkright(f, s):
            return s + 1 < len(tf[0]) and sample[f][s+1] != True
        def checkleft(f, s):
            return s - 1 >= 0 and sample[f][s-1] != True
        def checkup(f, s):
            return f - 1 >= 0 and sample[f-1][s] != True
        def checkdown(f, s):
            return f + 1 < len(tf) and sample[f+1][s] != True
        srow = 0
        scol = 0
        currval = 1
        dir = 'r'
        while currval <= n**2:
            tf[srow][scol] = currval
            sample[srow][scol] = True
            currval += 1
            if dir == 'r':
                if checkright(srow, scol):
                    scol += 1
                    continue
                elif checkdown(srow, scol):
                    dir = 'd'
                    srow += 1
                    continue
            if dir == 'd':
                if checkdown(srow, scol):
                    srow += 1
                    continue
                elif checkleft(srow, scol):
                    dir = 'l'
                    scol -= 1
                    continue
            if dir == 'u':
                if checkup(srow, scol):
                    srow -= 1
                    continue
                elif checkright(srow, scol):
                    dir = 'r'
                    scol += 1 
                    continue
            if dir == 'l':
                if checkleft(srow, scol):
                    scol -= 1
                    continue
                elif checkup(srow, scol):
                    srow -= 1
                    dir = 'u'
                    continue

        return tf
        