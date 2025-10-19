from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for element in strs:
            sorted_element = "".join(sorted(element))
            track[sorted_element].append(element)
        res = []
        for _, value in track.items():
            res.append(value)
        return res