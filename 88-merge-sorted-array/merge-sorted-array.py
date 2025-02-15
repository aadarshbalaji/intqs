class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        place = m + n - 1
        high = m-1
        low = n-1
        while low >= 0:
            if high >= 0 and nums2[low] < nums1[high]:
                nums1[place] = nums1[high]
                high -= 1
                place -= 1
            else:
                nums1[place] = nums2[low]
                low -= 1
                place -= 1
        
        
            