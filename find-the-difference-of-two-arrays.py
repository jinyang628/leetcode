from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter_one = set(nums1)
        counter_two = set(nums2)
        answer_one = []
        answer_two = []
        for element in counter_one:
            if element not in counter_two:
                answer_one.append(element)
        for element in counter_two:
            if element not in counter_one:
                answer_two.append(element)
        return [answer_one, answer_two]