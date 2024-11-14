class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        arr = []
        while x:
            arr.append(x % 10)
            x = x//10
        
        l = 0
        r = len(arr) - 1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True