class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        tf = matrix.copy()

        def checkright(f, s):
            return s + 1 < len(matrix[0]) and tf[f][s+1] != True
        def checkleft(f, s):
            print(s-1, tf[f][s-1])
            return s - 1 >= 0 and tf[f][s-1] != True
        def checkup(f, s):
            return f - 1 >= 0 and tf[f-1][s] != True
        def checkdown(f, s):
            return f + 1 < len(matrix) and tf[f+1][s] != True

        currf = 0
        currs = 0
        direct = 'r'
        rv = []
        while True:
            #print(tf, matrix)
            #print(matrix[currf][currs], direct)
            rv.append(matrix[currf][currs])
            tf[currf][currs] = True
            if direct == 'r':
                if checkright(currf, currs):
                    currs += 1
                    continue
                elif checkdown(currf, currs):
                    currf += 1
                    direct = 'd'
                    continue
            if direct == 'd':
                #print('here', currf, currs)
                if checkdown(currf, currs):
                    currf += 1
                    continue
                elif checkleft(currf, currs):
                    direct = 'l'
                    currs -= 1
                    continue
            if direct == 'l':
                if checkleft(currf, currs):
                    currs -= 1
                    continue
                elif checkup(currf, currs):
                    direct = 'u'
                    currf -= 1
                    continue
            if direct == 'u':
                if checkup(currf, currs):
                    currf -= 1
                    continue
                elif checkright(currf, currs):
                    direct = 'r'
                    currs += 1
                    continue
            break
            
        return rv
