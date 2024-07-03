class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        while tx > sx and ty > sy:
            if tx > ty:
                tx = tx % ty
            else:
                ty = ty % tx
        
        
        if ((tx==sx) and ((ty-sy) % sx == 0)) or ((ty == sy) and ((tx-sx) % sy == 0)):
            return True
        else:
            return False