class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = m + n - 1
        top = m-1
        bottom = n-1

        while bottom >= 0:
            if top >= 0 and nums1[top] > nums2[bottom]:
                nums1[r] =nums1[top]
                r -= 1
                top -= 1
            else:
                nums1[r] = nums2[bottom]
                bottom -= 1
                r -= 1

        