class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        max_odd = 0
        min_freq = float('inf')
        for _, value in count.items():
            if value % 2:
                max_odd = max(max_odd, value)
            else:
                min_freq = min(min_freq, value) 
        if min_freq == float('inf'):
            min_freq = 0
        return max_odd - min_freq