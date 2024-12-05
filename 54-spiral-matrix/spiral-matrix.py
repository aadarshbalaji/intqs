class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """        
        r = True
        d = False
        l = False
        u = False
        rv = []
        n = len(matrix)
        m = len(matrix[0])
        x,y = 0,0
        visited = set()
        visited.add((0,0))
        while len(rv) != n * m:
            rv.append(matrix[x][y])
            visited.add((x,y))
            if r:
                if (x, y+1) not in visited and y + 1 < m:
                    y += 1
                    continue
                else:
                    r = False
                    d = True
            if d:
                if (x+1, y) not in visited and x + 1 < n:
                    x += 1
                    continue
                else:
                    d = False
                    l = True
            if l:
                if (x, y-1) not in visited and y-1 >= 0:
                    y -= 1
                    continue
                else:
                    l = False
                    u = True
            if u:
                if (x-1, y) not in visited and x-1 >= 0:
                    x -= 1
                    continue
                else:
                    u = False
                    r = True
            if r:
                if (x, y+1) not in visited and y + 1 < m:
                    y += 1
                    continue
                else:
                    r = False
                    d = True
        return rv