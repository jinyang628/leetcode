class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        """
        overall = len(nums1) - 1
        second = len(nums2) - 1
        first = overall - second - 1
        while first >= 0 and second >= 0:
            if nums1[first] >= nums2[second]:
                nums1[overall] = nums1[first]
                first -= 1
            else:
                nums1[overall] = nums2[second]
                second -= 1
            overall -= 1
        while first >= 0:
            nums1[overall] = nums1[first]
            first -= 1
            overall -= 1
        while second >= 0:
            nums1[overall] = nums2[second]
            second -= 1
            overall -= 1