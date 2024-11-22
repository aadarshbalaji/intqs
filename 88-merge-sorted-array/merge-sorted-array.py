class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        place_here = m + n - 1
        topi = m-1
        bottomi = n-1
        while bottomi >= 0:
            if topi >=0  and nums2[bottomi] < nums1[topi]:
                nums1[place_here] = nums1[topi]
                topi -= 1
                place_here -= 1
            else:
                nums1[place_here] = nums2[bottomi]
                place_here -= 1
                bottomi -= 1
        