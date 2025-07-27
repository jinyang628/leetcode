class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        first = set()
        second = set()
        for num in nums1:
            if num not in nums2:
                first.add(num)
        for num in nums2:
            if num not in nums1:
                second.add(num)
        return [list(first), list(second)]