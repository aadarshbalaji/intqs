class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack