class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                l = 0
                r = len(stack) - 1
                index = None
                while l <= r:
                    mid = (l + r) // 2
                    if stack[mid] == num:
                        index = mid
                        break
                    if stack[mid] < num:
                        l = mid + 1
                    if stack[mid] > num:
                        r = mid - 1
                if not index:
                    index = l
                stack[index] = num
        return len(stack)