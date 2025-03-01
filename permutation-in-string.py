from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s1_counter = Counter(list(s1))
        print(s1_counter)
        def isPermutation(left: int, right: int) -> bool:
            s2_counter = Counter(list(s2[left: right]))
            for key, value in s1_counter.items():
                if s2_counter[key] != value:
                    return False
            return True
        while right <= len(s2):
            if isPermutation(left, right):
                return True
            left += 1
            right += 1
        return False