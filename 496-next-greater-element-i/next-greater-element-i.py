class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rv = [-1] * len(nums1)
        hs = {}
        for j, num1 in enumerate(nums1):
            hs[num1] = j
        stack = []
        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                rv[hs[stack.pop()]] = num
            if num in hs:
                stack.append(num)
        return rv
            

