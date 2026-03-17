1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
45        """
6        idx = len(nums2)
7        count = len(nums1) - 1
8        while count - idx >= 0:
9            nums1[count], nums1[count - idx] = nums1[count - idx], nums1[count]
10            count -= 1
1112        nums1_idx, nums2_idx = idx, 0
13        res_idx = 0
14        while nums1_idx < len(nums1) and nums2_idx < len(nums2):
15            if nums1[nums1_idx] <= nums2[nums2_idx]:
16                nums1[res_idx] = nums1[nums1_idx]
17                nums1_idx += 1
18            else:
19                nums1[res_idx] = nums2[nums2_idx]
20                nums2_idx += 1
21            res_idx += 1
22        while nums2_idx < len(nums2):
23            nums1[res_idx] = nums2[nums2_idx]
24            res_idx += 1
25            nums2_idx += 1
26