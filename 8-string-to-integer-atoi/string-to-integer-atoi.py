class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = s.lstrip()
        if not first:
            return 0
        pos = True
        if first[0] == '-':
            pos = False
            first = first[1:]
        elif first[0] == '+':
            first = first[1:]
            pos = True
        noleadingz = first.lstrip('0')
        read = ""
        print(noleadingz)
        for char in noleadingz:
            if char.isdigit():
                read += char
            else:
                break
        
        if not read:
            return 0
        if not pos:
            ans = -1 * int(read)
        else:
            ans = int(read)
        
        if ans < -(2**31):
            return -(2**31)
        elif ans > 2**31 - 1:
            return 2**31 - 1
        return ans
        

            
        