from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        track = Counter(arr)
        count = 0
        for element in arr:
            if track[element] == 1:
                count += 1
            if count == k :
                return element
        return ""