from collections import defaultdict
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        track = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                increment = 1 if nums1[i] == nums2[j] else 0
                track[(i, j)] =  max(
                    track[(i - 1, j - 1)] + increment,
                    track[(i - 1, j)],
                    track[(i, j - 1)]
                )
        return track[(len(nums1) - 1, len(nums2) - 1)]