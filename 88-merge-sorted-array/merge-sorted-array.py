class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        topi = m-1
        right = m + n -1
        bottomi = len(nums2) - 1
        while bottomi >= 0:
            if topi >= 0 and nums1[topi] > nums2[bottomi]:
                nums1[right] = nums1[topi]
                topi -=1
            else:
                nums1[right] = nums2[bottomi]
                bottomi -= 1
            right -= 1
        