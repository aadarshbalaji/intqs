class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s = s + s
        return len(goal) == len(s)//2 and goal in s