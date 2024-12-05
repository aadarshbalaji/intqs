class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        letters = list('abcdefghijklmnopqrstuvwxyza')
        bigger = 0
        smaller = 0
        def canmake(a,b):
            index = ord(a)-ord('a')
            if letters[index] == b or letters[index+1] == b:
                return True
            return False
        while True:
            if bigger >= len(str1) or smaller >= len(str2):
                break
            if canmake(str1[bigger], str2[smaller]):
                bigger += 1
                smaller += 1
            else:
                bigger += 1
        
        return smaller >= len(str2)
            