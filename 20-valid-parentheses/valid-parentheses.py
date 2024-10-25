class Solution:
    def isValid(self, s: str) -> bool:
        o = ['(', '{' , '[']
        c = [')', '}', ']']
        mapping = {y:x for x,y in zip(o,c)}
    
        q = deque()
        for c in s:
            if c in o:
                q.append(c)
            elif c in c:
                if len(q) == 0:
                    return False
                if mapping[c] != q.pop():
                    return False
        if len(q) == 0:
            return True
        else:
            return False
            