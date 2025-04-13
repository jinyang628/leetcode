class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if not nums1:
            if len(nums2) % 2 == 1:
                return float(nums2[len(nums2) // 2])
            return float((nums2[len(nums2) // 2] + nums2[(len(nums2) // 2) - 1]) / 2)
        left = 0
        right = len(nums1)
        total_length = len(nums1) + len(nums2)
        partition_size = (total_length + 1) // 2
        while left <= right:
            mid = left + (right - left) // 2
            nums2_mid = partition_size - mid
            left_one = float('-inf') if mid == 0 else nums1[mid - 1]
            right_one = float('inf') if mid == len(nums1) else nums1[mid]
            left_two = float('-inf') if nums2_mid == 0 else nums2[nums2_mid - 1]
            right_two = float('inf') if nums2_mid == len(nums2) else nums2[nums2_mid]
            if left_one <= right_two and left_two <= right_one:
                if total_length % 2 == 1:
                    return float(max(left_one, left_two))
                return float((max(left_one, left_two)+ min(right_one, right_two)) / 2)
            elif left_one > right_two:
                right = mid - 1
            else:
                left = mid + 1