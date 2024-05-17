class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        count = {chr(c):0 for c in range(ord('a'),ord('a')+26)}
        correct = {chr(c):0 for c in range(ord('a'),ord('a')+26)}
        for l in s1:
            correct[l] += 1
        left = 0
        right = len(s1) - 1
        if right + 1 > len(s2):
            return False
        for letter in s2[left:right +1]:
            count[letter] += 1
        while right + 1 < len(s2):
            #print(s2[left:right +1])
            #print(left,right)
            if correct == count:
                return True
            count[s2[left]] -= 1
            left += 1
            count[s2[right + 1]] += 1
            right += 1
        return correct == count
            
        