class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for j in range(len(digits)-1, -1, -1):
            if digits[j] == 9 and carry:
                digits[j] = 0 
                carry = 1
            else:
                digits[j] += carry
                carry = 0
        
        if carry and digits[0] == 0:
            return [1] + digits
        return digits