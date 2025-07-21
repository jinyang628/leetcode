class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        """
        nums1_pointer = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[nums1_pointer] = nums1[m]
                m -= 1
            else:
                nums1[nums1_pointer] = nums2[n]
                n -= 1
            nums1_pointer -= 1
        while m >= 0:
            nums1[nums1_pointer] = nums1[m]
            nums1_pointer -= 1
            m -= 1
        while n >= 0:
            nums1[nums1_pointer] = nums2[n]
            nums1_pointer -= 1
            n -= 1
        return nums1