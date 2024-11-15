class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        top = m - 1
        bottom = n-1
        right = m + n - 1

        while bottom >= 0:
            if top >= 0 and nums1[top] > nums2[bottom]:
                nums1[right] = nums1[top]
                top -= 1
            else:
                nums1[right] = nums2[bottom]
                bottom -= 1
            right -= 1
        


        